# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:07:26 2013

@author: VHOEYS

pltofunctions to support visual inspection
"""

from itertools import cycle, count
from scipy.stats import pearsonr, spearmanr, kendalltau
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, LinearLocator, NullLocator, FixedLocator
from matplotlib.patches import Rectangle, Polygon
from scipy import stats
import pylab as p

def _definedec(nummin,nummax):
    '''
    Help function to define the number of shown decimals
    '''
    diff = nummax - nummin
    predec = len(str(diff).split('.')[0])
    if predec > 1:
        dec = -(predec-1)
    else:
        if str(diff)[0] <> '0':
            dec = 1
        else:
            cnt = 1
            for char in str(diff).split('.')[1]:
                if char == '0':
                    cnt+=1
            dec = cnt
    return dec

def scatterplot_matrix(data1, plottext=None, limin = False, upperpane = 'pearson',
                             limax = False,  plothist = False, layout = 'full', 
                             *args, **kwargs):
    """
    Plots a scatterplot matrix of subplots.  Each row of "data" is plotted
    against other rows, resulting in a nrows by nrows grid of subplots.
    
    Still some work: *only half of it showing + hide subplots upper half
        
    Parameters
    -----------
    data1 : ndarray
        numvars rows and numdata columns datapoints to compare,
        when only this dataset is given, the dat is plotted twice in the 
        graph
    plottext : None | list
        list of strings woth the text to put for the variables, when no 
        histograms are needed
    limin : False | list 
        List of user defined minimal values for the different
        variables. When False, the min/max values are calculated
    limax : False | list 
        List of user defined maximal values for the different
        variables. When False, the min/max values are calculated 
    plothist : bool
        histogram is plotted in the middle of the data1 when True
    layout : full|half
        full doubles the visualisation, half only shows the lower half of 
        the scattermatrix
    upperpane : pearson|spearman|kendall|data
        Decision about the content of the upper pane of the graph; implemented
        are pearson, spearman, kendall correlation coefficients; when data is
        chosen, the data is plotted again
    *args, **kwargs: arg
        arguments passed to the scatter method 
    
    Returns
    ---------
    fig: matplotlib.figure.Figure object
        figure containing the output
    axes: array of matplotlib.axes.AxesSubplot object
        enabled post-processing of the ax-elements
        
    Examples
    ---------
    >>> np.random.seed(1977)
    >>> numvars, numdata = 4, 1111
    >>> data1 = 5 * np.random.normal(loc=3.,scale=2.0,size=(numvars, numdata))
    >>> fig,axes = scatterplot_matrix(data1, marker='o', color='black', mfc='none', upperpane = 'kendall',
                                  layout = 'full', plothist = True, plottext=['A','B','C','D'])
    >>> ax2add = axes[0,0]
    >>> ax2add.text(0.05,0.8,r'$some_{\alpha}$',transform = ax2add.transAxes,
                    fontsize=20)
    
    Notes
    ------
    typically used for comparing objective functions outputs, or parameter 
    distributions
    
    When using two datasets, only useful ticks when the datalimits
    are more or less the same, since otherwise the plot won't show both nicely
    """
       
   
    numvars, numdata = data1.shape
    fig, axes = plt.subplots(nrows=numvars, ncols=numvars, figsize=(20,20))
#    fig.subplots_adjust(hspace=0.05, wspace=0.03)
    fig.subplots_adjust(hspace=0., wspace=0.0)

    for ax in axes.flat:
        # Hide all ticks and labels
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
           
        if ax.is_first_col():
            ax.yaxis.set_ticks_position('left')
        if ax.is_last_col():
            ax.yaxis.set_ticks_position('right')
        if ax.is_first_row():
            ax.xaxis.set_ticks_position('top')
        if ax.is_last_row():
            ax.xaxis.set_ticks_position('bottom')
        #adjust the ticker lengths and position
        ax.tick_params(direction = 'out', pad=8, length = 5., 
                       color = 'black', which = 'major')
        ax.tick_params(length = 3., which = 'minor')

    #calc datalimits
    if not isinstance(limin, list) or not isinstance(limax,list):
        limin=[]
        limax=[]        
        for i in range(data1.shape[0]):
                dec1 = _definedec(np.min(data1[i]),np.max(data1[i]))
                limin.append(np.around(np.min(data1[i]),decimals = dec1))
                limax.append(np.around(np.max(data1[i]),decimals = dec1))
        print 'used limits are', limin,'and', limax
    else:
        print 'used limits are', limin,'and', limax          
    
    # Plot the data.
    for i, j in zip(*np.triu_indices_from(axes, k=1)):
#        for x, y in [(i,j), (j,i)]:
        for x, y in [(j,i)]: #low  
            axes[x,y].plot(data1[y], data1[x], linestyle='none', *args, **kwargs)
            axes[x,y].set_ylim(limin[x],limax[x])
            axes[x,y].set_xlim(limin[y],limax[y])
                          
        for x, y in [(i,j)]:           
            if layout == 'full':
                if upperpane == 'pearson': #default
                    axes[x,y].text(0.5,0.5, r'%.3f'%pearsonr(data1[y], data1[x])[0],
                        horizontalalignment='center', verticalalignment='center',
                                    transform = axes[x,y].transAxes, fontsize=14, alpha = 0.5)
                elif upperpane == 'spearman':
                    axes[x,y].text(0.5,0.5, r'%.3f'%spearmanr(data1[y], data1[x])[0],
                        horizontalalignment='center', verticalalignment='center',
                                    transform = axes[x,y].transAxes, fontsize=14, alpha = 0.5)
                elif upperpane == 'kendall':
                    try:
                        kendal, kendalp = kendalltau(data1[y], data1[x])
                        axes[x,y].text(0.5,0.5, r'%.3f'%kendal,
                            horizontalalignment='center', verticalalignment='center',
                                        transform = axes[x,y].transAxes, fontsize=14, alpha = 0.5)   
                    except:
                        kendal = 'nan'
                        axes[x,y].text(0.5,0.5, kendal,
                            horizontalalignment='center', verticalalignment='center',
                                        transform = axes[x,y].transAxes, fontsize=14)    
                elif upperpane == 'data':
                    axes[x,y].plot(data1[y], data1[x], linestyle='none', *args, **kwargs)  
                else:
                    axes[x,y].plot(data1[y], data1[x], linestyle='none', *args, **kwargs)  
                    print 'data is plotted again, since no correlation coefficent was selected'
                    
            elif layout == 'half':
                print 'upperpane is hidden'
                axes[x,y].set_axis_off()
            axes[x,y].set_ylim(limin[x],limax[x])
            axes[x,y].set_xlim(limin[y],limax[y]) 

    #PLOT histograms  and variable names  
    #    for i, label in enumerate(plottext):   
    for i in range(numvars):
        if not plothist and plottext:
            label = plottext[i]
            axes[i,i].annotate(label, (0.5, 0.5), xycoords='axes fraction',
                    ha='center', va='center', fontsize = 16)
        else: #plot histogram in center
            axes[i,i].hist(data1[i],bins=20,color='k')
            axes[i,i].set_xlim(limin[i],limax[i])
                
    if plothist:
        print 'plottext is not visible'

    # Turn on the proper x or y axes ticks.
    if layout == 'full':
        for i, j in zip(range(numvars), cycle((-1, 0))):
            axes[j,i].xaxis.set_visible(True)
            axes[i,j].yaxis.set_visible(True)
                 
            majorLocator = LinearLocator(3)
            axes[j,i].xaxis.set_major_locator(majorLocator)
            axes[i,j].yaxis.set_major_locator(majorLocator)
    
            minorLocator  = LinearLocator(11)
            axes[j,i].xaxis.set_minor_locator(minorLocator)
            axes[i,j].yaxis.set_minor_locator(minorLocator)   
    else: #layout half
        for i, j in zip(count(1), range(numvars-1)):
            axes[-1,j].xaxis.set_visible(True)
            axes[-1,j].set_xlim(limin[j]-0.1*(limax[j]-limin[j]),limax[j]+0.1*(limax[j]-limin[j]))
            majorLocator2= FixedLocator([limin[j], limax[j]])
            minorLocator  = FixedLocator(np.linspace(limin[j], limax[j],10))
            axes[-1,j].xaxis.set_major_locator(majorLocator2) 
            axes[-1,j].xaxis.set_minor_locator(minorLocator)            

            axes[i,0].yaxis.set_visible(True)
            axes[i,0].set_ylim(limin[i]-0.1*(limax[i]-limin[i]),limax[i]+0.1*(limax[i]-limin[i]))
            majorLocator3= FixedLocator([limin[i], limax[i]])
            minorLocator  = FixedLocator(np.linspace(limin[i], limax[i],10))            
            axes[i,0].yaxis.set_major_locator(majorLocator3)
            axes[i,0].yaxis.set_minor_locator(minorLocator)  
              
    #When uneven, some changes needed to properly put the ticks and tickslabels
    #since the ticks next to the histogram need to take the others y-scale
    #solved by adding a twinx taking over the last limits
    if not numvars%2==0 and layout == 'full':# and plothist==False:  
        if plothist == False:
            #create dummy info when no histogram is added
            axes[numvars-1,numvars-1].set_xlim(limin[numvars-1], 
                                        limax[numvars-1])
            axes[numvars-1,numvars-1].set_ylim(limin[numvars-1], 
                                        limax[numvars-1])
            
        axextra = axes[numvars-1,numvars-1].twinx()
        axextra.set_ylim(limin[numvars-1],limax[numvars-1])
        axextra.yaxis.set_minor_locator(minorLocator)
        axextra.yaxis.set_major_locator(majorLocator)
        
        axes[numvars-1,numvars-1].yaxis.set_ticks([])
        axes[numvars-1,numvars-1].yaxis.set_minor_locator(NullLocator())    
        
        axes[numvars-1,numvars-1].xaxis.set_major_locator(majorLocator)
        axes[numvars-1,numvars-1].xaxis.set_minor_locator(minorLocator)                
    return fig, axes   


def Spread_diagram(axs,obs, mod, infobox = True, *args, **kwargs):
    '''
    Adapted from pySTAN-Packages, author: Van Hoey Stijn
    
    Plot a scatter plot comparing the modelled and observed datasets in a 
    scatter plot. 
    
    Parameters
    -----------
    axs : axes.AxesSubplot object
        an subplot instance where the graph will be located,
        this supports the use of different subplots
    obs : ndarray
        1D array of the observed data
    mod : ndarray
        1D array of the modelled output
    infobox : bool True|False
        defines if a infobox with the regression info is added or not
    *args, **kwargs : args
        argument passed to the matplotlib scatter command
    
    Returns
    --------
    axs
    
    Examples
    ---------
    >>> obs = 20*np.random.random(200)
    >>> mod = 0.8*obs + 2 * np.random.random(200) -1
    >>> fig = plt.figure()
    >>> axs = fig.add_subplot(111)
    >>> axs = Spread_diagram(axs, obs, mod, infobox = True, 
                             marker='o', facecolor='none', 
                             edgecolor = 'k')
    >>> axs.set_xlabel(r'observed ($m^3 s^{-1}$)')                     
    >>> axs.set_ylabel(r'modelled ($m^3 s^{-1}$)') 
    
    '''
    p.rc('mathtext', default='regular')    
       
    axs.scatter(obs,mod, *args, **kwargs)
    axs.set_aspect('equal')
    
    getmax = max(obs.max(),mod.max())*1.1
    getmin = min(obs.min(),mod.min())*0.9
    axs.plot([getmin,getmax],[getmin,getmax],'k--', linewidth = 0.5)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(obs, mod)
#    m,b = p.polyfit(obs, mod, 1)
    forplot = np.arange(getmin,getmax,0.01)
    axs.plot(forplot, slope*forplot+intercept, '-', color='grey', 
             linewidth = 0.5)  
    axs.set_xlim(left = getmin, right=getmax)
    axs.set_ylim(bottom = getmin, top=getmax)   
    
    rmse = np.sqrt((np.sum((obs-mod)**2))/obs.size)
    
    
    #for infobox
    if infobox == True:
        patch=Rectangle((0., 0.65), .35, 0.35, facecolor = 'white',
                        edgecolor='k', transform=axs.transAxes)
        axs.add_patch(patch)
        axs.set_axisbelow(True)
        
        textinfo = ({'transform' : axs.transAxes, 'verticalalignment':'center', 
                    'horizontalalignment':'left', 'fontsize':12})
                  
        axs.text(0.05, 0.95, r'$\bar{x}\ $', textinfo) 
        axs.text(0.05, 0.90, r'$\bar{y}\ $', textinfo)           
        axs.text(0.05, 0.85, r'$rico\ $', textinfo)             
        axs.text(0.05, 0.8, r'$intc.\ $', textinfo)  
        axs.text(0.05, 0.75, r'$R^2\ $', textinfo)               
        axs.text(0.05, 0.70, r'$RMSE\ $', textinfo)   
    
        axs.text(0.2, 0.95, r': %.2f'%obs.mean(), textinfo) 
        axs.text(0.2, 0.90, r': %.2f'%mod.mean(), textinfo)           
        axs.text(0.2, 0.85, r': %.2f'%slope, textinfo)             
        axs.text(0.2, 0.8, r': %.2f'%intercept, textinfo)  
        axs.text(0.2, 0.75, r': %.2f'%r_value, textinfo)               
        axs.text(0.2, 0.70, r': %.2f'%rmse, textinfo)    

    return axs    