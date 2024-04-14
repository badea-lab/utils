"""
A top level utility script to format root plots. Include this file in your plotting script to gain access.
"""
import os
import ROOT
###################### Environment Style ######################
def atlasstyle():
    ''' General ATLAS plotting environment '''
    ROOT.gStyle.SetPaintTextFormat("0.3f")
    ROOT.gStyle.SetPadTickX(1)
    ROOT.gStyle.SetPadTickY(1)
    icol=0
    ROOT.gStyle.SetFrameBorderMode(icol);
    ROOT.gStyle.SetFrameFillColor(icol);
    ROOT.gStyle.SetCanvasBorderMode(icol);
    ROOT.gStyle.SetCanvasColor(icol);
    ROOT.gStyle.SetPadBorderMode(icol);
    ROOT.gStyle.SetPadColor(icol);
    ROOT.gStyle.SetStatColor(icol);
    ROOT.gStyle.SetPalette(ROOT.kRainBow)
    #set the paper & margin sizes
    ROOT.gStyle.SetPaperSize(20,26);

    # set margin sizes
    ROOT.gStyle.SetPadTopMargin(0.05);
    ROOT.gStyle.SetPadRightMargin(0.05);
    ROOT.gStyle.SetPadBottomMargin(0.16);
    ROOT.gStyle.SetPadLeftMargin(0.16);

    # set title offsets (for axis label)
    ROOT.gStyle.SetTitleXOffset(1.4);
    ROOT.gStyle.SetTitleYOffset(1.4);

    # use large fonts
    font=72; # Helvetica italics
    font=42; # Helvetica
    tsize=0.05;
    ROOT.gStyle.SetTextFont(font);

    ROOT.gStyle.SetTextSize(tsize);
    ROOT.gStyle.SetLabelFont(font,"x");
    ROOT.gStyle.SetTitleFont(font,"x");
    ROOT.gStyle.SetLabelFont(font,"y");
    ROOT.gStyle.SetTitleFont(font,"y");
    ROOT.gStyle.SetLabelFont(font,"z");
    ROOT.gStyle.SetTitleFont(font,"z");

    ROOT.gStyle.SetLabelSize(tsize,"x");
    ROOT.gStyle.SetTitleSize(tsize,"x");
    ROOT.gStyle.SetLabelSize(tsize,"y");
    ROOT.gStyle.SetTitleSize(tsize,"y");
    ROOT.gStyle.SetLabelSize(tsize,"z");
    ROOT.gStyle.SetTitleSize(tsize,"z");

    # use bold lines and markers
    ROOT.gStyle.SetMarkerStyle(20);
    ROOT.gStyle.SetMarkerSize(1.2);
    ROOT.gStyle.SetHistLineWidth(2);
    ROOT.gStyle.SetLineStyleString(2,"[12 12]"); # postscript dashes

    # get rid of X error bars (as recommended in ATLAS figure guidelines)
    ROOT.gStyle.SetErrorX(0.0001);
    # get rid of error bar caps
    ROOT.gStyle.SetEndErrorSize(0.);

    # do not display any of the standard histogram decorations
    ROOT.gStyle.SetOptTitle(0);
    # ROOT.gStyle.SetOptStat(1111);
    ROOT.gStyle.SetOptStat(0);
    # ROOT.gStyle.SetOptFit(1111);
    ROOT.gStyle.SetOptFit(0);

    # put tick marks on top and RHS of plots
    ROOT.gStyle.SetPadTickX(1);
    ROOT.gStyle.SetPadTickY(1);

###################### Legend ######################
def legend(loc):
    ''' Make a legend a give location [x1,y1,x2,y2] '''
    l = ROOT.TLegend(loc[0],loc[1],loc[2],loc[3])
    l.SetFillStyle(0);
    l.SetBorderSize(0);
    l.SetTextSize(0.038);
    return l

###################### Histogram ######################
def format_hist(
    h,
    title="",
    x_title="x_title",
    x_title_offset=0,
    x_title_size=0.05,
    x_label_size=0.05,
    x_n_divisions=505,
    x_min=None,
    x_max=None,
    x_tick_length=0.03,
    y_title="y_title",
    y_title_offset=0,
    y_title_size=0.05,
    y_label_size=0.05,
    y_n_divisions=505,
    y_tick_length=0.03,
    y_min=None,
    y_max=None,
    z_title="z_title",
    z_title_offset=0,
    z_title_size=0.05,
    z_label_size=0.05,
    z_n_divisions=505,
    z_min=None,
    z_max=None,
    z_tick_length=0.03,
    title_font=82,
    label_font=82,
    line_color=1,
    line_width=3,
    fill_style=1001,
    fill_color=0,
):
    ''' Histogram formatter '''
    if type(h) == ROOT.TH1D:
        h.SetStats(False)

    h.SetTitle(title)

    h.GetXaxis().SetTitle(x_title)
    h.GetXaxis().SetTitleFont(title_font)
    h.GetXaxis().SetTitleOffset(x_title_offset)
    h.GetXaxis().SetTitleSize(x_title_size)
    h.GetXaxis().CenterTitle()
    h.GetXaxis().SetLabelSize(x_label_size)
    h.GetXaxis().SetLabelFont(label_font)
    h.GetXaxis().SetNdivisions(x_n_divisions)
    h.GetXaxis().SetTickLength(x_tick_length)
    if x_min is not None: h.GetXaxis().SetRangeUser(x_min,x_max)

    h.GetYaxis().SetTitle(y_title)
    h.GetYaxis().SetTitleFont(title_font)
    h.GetYaxis().SetTitleOffset(y_title_offset)
    h.GetYaxis().SetTitleSize(y_title_size)
    h.GetYaxis().CenterTitle()
    h.GetYaxis().SetLabelSize(y_label_size)
    h.GetYaxis().SetLabelFont(label_font)
    h.GetYaxis().SetNdivisions(y_n_divisions)
    h.GetYaxis().SetTickLength(y_tick_length)
    if y_min is not None: h.GetYaxis().SetRangeUser(y_min,y_max);

    if type(h) == ROOT.TH2D:
        h.GetZaxis().SetTitle(z_title)
        h.GetZaxis().SetTitleFont(title_font)
        h.GetZaxis().SetTitleOffset(z_title_offset)
        h.GetZaxis().SetTitleSize(z_title_size)
        h.GetZaxis().CenterTitle()
        h.GetZaxis().SetLabelSize(z_label_size)
        h.GetZaxis().SetLabelFont(label_font)
        h.GetZaxis().SetNdivisions(z_n_divisions)
        h.GetZaxis().SetTickLength(z_tick_length)
        if z_min is not None: h.SetMinimum(z_min)
        # h.SetMinimum(z_min)
        # h.SetMaximum(z_max)

    h.SetLineColor(line_color)
    h.SetLineWidth(3)
    h.SetFillStyle(fill_style)
    h.SetFillColor(fill_color)

def style2d():
    style = { 
        "title": "",
        "x_title_offset": 1.1,
        "x_label_size": 0.04,
        "y_title_offset": 1.,
        "y_label_size": 0.04,
        "z_title_offset": 1.25,
        "z_label_size": 0.04,
        "z_min": 0,
        "z_max": 1,
        "title_font": 42,
        "label_font": 42 
    }
    return style

def style1d():
    style = { 
        "title": "",
        "x_title_offset": 1.1,
        "x_label_size": 0.04,
        "y_title_offset": 1.4,
        "y_label_size": 0.04,
        "title_font": 42,
        "label_font": 42,
        "fill_color": 0 
    }
    return style

###################### Canvas ######################
def canv(name,x=1700,y=1400,lm=0.15,rm=0.18,tm=0.05,bm=0.12):
    ''' Return a formatted canvas '''
    c = ROOT.TCanvas(name, name, x, y)
    c.SetLeftMargin(lm)
    c.SetRightMargin(rm)
    c.SetTopMargin(tm)
    c.SetBottomMargin(bm)
    return c

###################### Labeling ######################
def format_text(hist):
    if isinstance(hist, ROOT.TLatex):
        hist.SetTextSize(0.015)
        hist.SetTextFont(42)
        return

def atlasinternal(x=0.665,y=0.96):
    ''' Place an ATLAS internal label on the upper right hand side of the plot '''
    a = ROOT.TLatex(x, y, "#bf{ATLAS} Internal")
    a.SetTextFont(42)
    a.SetNDC()
    a.SetTextColor(ROOT.kBlack)
    a.SetTextSize(0.030)
    return a

def myText(x, y, color, text, tsize):
    l = ROOT.TLatex() 
    #l.SetTextAlign(12); 
    l.SetTextSize(tsize); 
    l.SetNDC();
    l.SetTextColor(color);
    l.DrawLatex(x,y,text);
    return l
