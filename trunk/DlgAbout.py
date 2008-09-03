# -*- coding: iso-8859-1 -*-

__version__ ='$Rev: 31 $'
__date__ = '$LastChangedDate: 2008-09-03 12:31:48 -0300 (qua, 03 set 2008) $'

#Boa:Dialog:AboutDlg

import wx

def create(parent):
    return AboutDlg(parent)

[wxID_ABOUTDLG, wxID_ABOUTDLGBTNOK, wxID_ABOUTDLGDESCTXT, 
 wxID_ABOUTDLGTEXTCTRL1, wxID_ABOUTDLGTITUTXT, wxID_ABOUTDLGVERSAOTXT, 
] = [wx.NewId() for _init_ctrls in range(6)]

class AboutDlg(wx.Dialog):
    def _init_coll_flexGridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.TituTxt, 0, border=4,
              flag=wx.ALIGN_CENTER | wx.ALL)
        parent.AddWindow(self.VersaoTxt, 0, border=4,
              flag=wx.EXPAND | wx.ALL | wx.ALIGN_CENTER)
        parent.AddWindow(self.DescTxt, 1, border=4,
              flag=wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
        parent.AddWindow(self.textCtrl1, 0, border=4,
              flag=wx.EXPAND | wx.ALIGN_CENTER | wx.ALL)
        parent.AddWindow(self.BtnOk, 0, border=4, flag=wx.ALIGN_CENTER | wx.ALL)

    def _init_coll_flexGridSizer1_Growables(self, parent):
        # generated method, don't edit

        parent.AddGrowableRow(2)
        parent.AddGrowableRow(3)
        parent.AddGrowableCol(0)

    def _init_sizers(self):
        # generated method, don't edit
        self.flexGridSizer1 = wx.FlexGridSizer(cols=1, hgap=0, rows=5, vgap=0)

        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_flexGridSizer1_Growables(self.flexGridSizer1)

        self.SetSizer(self.flexGridSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ABOUTDLG, name='AboutDlg', parent=prnt,
              pos=wx.Point(496, 391), size=wx.Size(364, 414),
              style=wx.DEFAULT_DIALOG_STYLE, title='Sobre o LabControle')
        self.SetClientSize(wx.Size(356, 386))

        self.TituTxt = wx.StaticText(id=wxID_ABOUTDLGTITUTXT,
              label='LabControle', name='TituTxt', parent=self,
              pos=wx.Point(114, 4), size=wx.Size(128, 23), style=0)
        self.TituTxt.SetFont(wx.Font(16, wx.SWISS, wx.ITALIC, wx.BOLD, False,
              'Arial'))

        self.textCtrl1 = wx.TextCtrl(id=wxID_ABOUTDLGTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(4, 177),
              size=wx.Size(348, 166), style=wx.TE_READONLY, value='textCtrl1')

        self.BtnOk = wx.Button(id=wx.ID_OK, label='OK', name='BtnOk',
              parent=self, pos=wx.Point(136, 351), size=wx.Size(84, 30),
              style=0)

        self.VersaoTxt = wx.StaticText(id=wxID_ABOUTDLGVERSAOTXT,
              label='Vers\xe3o: 1.0 r31', name='VersaoTxt', parent=self,
              pos=wx.Point(4, 35), size=wx.Size(348, 19),
              style=wx.ALIGN_CENTRE)
        self.VersaoTxt.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Arial'))
        self.VersaoTxt.SetHelpText('')

        self.DescTxt = wx.StaticText(id=wxID_ABOUTDLGDESCTXT, label='Descricao',
              name='DescTxt', parent=self, pos=wx.Point(4, 62),
              size=wx.Size(348, 107), style=0)
        self.DescTxt.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        descricao = """O LabControle � um programa simulador de sistemas de controle lineares e invariantes no tempo. Foi desenvolvido por Miguel Moreto na Universidade Federal de Santa Catarina.
        Este software est� registrado sob GNU General Public Licenese."""
        
        self.DescTxt.SetLabel(descricao)
        self.Layout()
