#!/bin/env python

from plot_inputs import *

def main():

    hists=[
    'GEN/h1_Gen_TauAllFromH_Eta_SubLead',
    ]

    binning={
    }

    xranges={
        "GEN/h1_Gen_TauAllFromH_Eta_SubLead":[-2.5,2.5],    
    }

    for hist in hists:
        print("Now plotting: " + hist)
        histContainer.getHist(hist)

        binf=getDictValue(hist,binning)
        if binf is not None:
            #dat_hist.rebin(width=1,vector=binf)
            bghists.rebin(binf)
            sghist.rebin(binf)

        hist_style = sc.style_container(style = 'CMS', useRoot = False,cms=13,lumi=lumi, cmsPositon = 'upper left')
        hist_style.Set_n_legend_columns(3)

        #dummy = bghists.getAllAdded()
        #dummy.xaxis.SetTitle('')
        #dummy.yaxis.SetTitle('')
        #dummy.SaveAs('plots/' + hist.replace("/","") + '.root')

        #test = plotter(hist=bghists.getHistList(), sig = sghist.getHistList(),style=hist_style)
        test  = plotter(sig=sghist.getHistList(), style=hist_style)
        #test.Add_data(dat_hist.getHistList()[0])

        hist_style.Set_error_bands_fcol(['gray','orange'])
        hist_style.Set_error_bands_ecol(['black','black'])
        hist_style.Set_error_bands_labl(['Systematics','Statistic'])

 #       if hist == 'emu/Stage_0/h1_0_emu_Mass':
 #           sys_file=File('syst/for_plotting.root', "read")
        
 #           test.Add_error_hist([sys_file.Get('Sys'),sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')
            # test.Add_error_hist([sys_file.Get('MC statistic')], band_center = 'ref', stacking = 'Nosum')

 #       test.Add_plot('Diff',pos=0, height=12)

 #       test.Add_plot('DiffRatio',pos=1, height=12)
 #       test.Add_plot('Signi',pos=2, height=12)

        if hist in xranges.keys():
            test.Set_axis(logx=False,logy=True,xmin=xranges[hist][0],xmax=xranges[hist][1],ymin=1e-6,ymax=1e3)
            ##test.Set_axis(logx=False,logy=True,xmin=xranges[hist][0],xmax=xranges[hist][1])

        name=hist.replace("/","")

        test.create_plot()

     #   test.Get_axis0().set_ylim(ymin = -1.2, ymax = 1.7)
     #   test.Get_axis2().set_ylim(ymin = -3, ymax = 13)
     #   test.Get_axis3().set_ylim(ymin = -3, ymax = 3.0)

        test.SavePlot('plots/%s.pdf'%(name))
        test.SavePlot('plots/%s.png'%(name))

    return 42



main()
