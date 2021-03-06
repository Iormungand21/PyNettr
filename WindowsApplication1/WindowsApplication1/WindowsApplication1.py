import clr

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import Color, Size, Icon, Font, FontStyle, Point
from System.Windows.Forms import *
from System import Environment


class FormOne(Form):
    def __init__(self):

        # Colors
        self.color_title = Color.FromArgb(135, 189, 68)
        self.color_button_sel = Color.FromArgb(153, 198, 91)
        self.color_button = Color.FromArgb(103, 148, 41)
        self.color_window = Color.FromArgb(48, 48, 48)
        self.color_panel = Color.FromArgb(124, 124, 124)

        # Window parameters
        self.Text = "PyNettr 0.1.0"
        self.Name = "Test"
        self.Size = Size(500, 550)
        self.MinimumSize = Size(460, 480)
        self.BackColor = self.color_window
        self.Icon = Icon("res\\icon.ico")

        # Top Main Label
        self.top_label = Label()
        self.top_label.Anchor = AnchorStyles.Top
        self.top_label.Text = "PyNettr"
        self.top_label.Size = Size(120, 30)
        self.top_label.ForeColor = self.color_title
        self.top_label.Font = Font("Lucida Console", 16, FontStyle.Bold)
        self.top_label.Location = Point(185, 3)

        # Console box to write to
        self.console_box = self.new_textbox()
        self.console_box.Multiline = True
        self.console_box.ReadOnly = True
        self.console_box.BackColor = Color.FromArgb(65, 65, 65)
        self.console_box.ScrollBars = ScrollBars.Vertical
        self.console_box.Size = Size(420, 120)
        self.console_box.Location = Point(30, 360)
        self.console_box.Anchor = (AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom)

        self.acl_panel_new = self.setup_acl_tool()

        # Placeholder_1 Tool panel#################################
        self.placeholder_panel_1 = self.new_panel()
        self.placeholder_panel_1.Name = "placeholder_panel_1"

        # Placeholder_2 Tool Panel##################################
        self.placeholder_panel_2 = self.new_panel()
        self.placeholder_panel_2.Name = "placeholder_panel_2"

        # Placeholder_3 Tool Panel##################################
        self.placeholder_panel_3 = self.new_panel()
        self.placeholder_panel_3.Name = "placeholder_panel_3"



        # Main Tool Buttons######################################
        # Button to activate ACL tool panel
        self.button_acl_tool = self.new_button()
        self.button_acl_tool.Text = "ACL Tool"
        self.button_acl_tool.Location = Point(30, 37)
        self.button_acl_tool.Click += self.acl_tool

        # Button to activate X tool panel
        self.button_ph_tool_1 = self.new_button()
        self.button_ph_tool_1.Text = "Test"
        self.button_ph_tool_1.Location = Point(138, 37)
        self.button_ph_tool_1.Click += self.placeholder_tool_1

        # Button for phtool2
        self.button_ph_tool_2 = self.new_button()
        self.button_ph_tool_2.Location = Point(247, 37)
        self.button_ph_tool_2.Text = "Test2"
        #self.button_ph_tool_2.Click += self.placeholder_tool_2

        # Button for tool_4
        self.button_tool_4 = self.new_button()
        self.button_tool_4.Location = Point(358, 37)
        self.button_tool_4.Text = "Tool_4"
        self.button_tool_4.Click += self.activate_tool_4

        self.tool_4_panel = self.setup_tool_4()


        # Adding initial layout##################################
        self.Controls.Add(self.top_label)
        # buttons
        self.Controls.Add(self.button_acl_tool)
        self.Controls.Add(self.button_ph_tool_1)
        self.Controls.Add(self.button_ph_tool_2)
        self.Controls.Add(self.button_tool_4)
        # panels
        self.Controls.Add(self.placeholder_panel_1)
        self.Controls.Add(self.placeholder_panel_2)

        self.Controls.Add(self.tool_4_panel)
        self.Controls.Add(self.acl_panel_new)
        self.Controls.Add(self.console_box)

    def setup_tool_4(self):
        panel = self.new_panel()
        panel.Name = "tool_4_panel"
        radio1 = self.new_radio()
        radio1.Name = "test"
        radio1.Location = Point(40, 50)
        panel.Controls.Add(radio1)
        return panel

    def setup_acl_tool(self):
        self.acl = self.new_panel()
        self.acl.Name = "tool_acl"

        # ACL name label
        self.acl_label = self.new_label()
        self.acl_label.Location = Point(14, 14)
        self.acl_label.Size = Size(79, 15)
        self.acl_label.Text = "ACL Name:"

        # ACL name field
        self.acl_field_name = self.new_textbox()
        self.acl_field_name.Location = Point(100, 11)
        self.acl_field_name.Size = Size(300, 20)
        self.acl_field_name.Text = "Outside_access_in"

        # Protocol radio buttons
        self.acl_radio_tcp = self.new_radio()
        self.acl_radio_tcp.Name = "acl_radio_tcp"
        self.acl_radio_tcp.Text = "TCP"
        self.acl_radio_tcp.Location = Point(10, 17)

        self.acl_radio_udp = self.new_radio()
        self.acl_radio_udp.Name = "acl_radio_udp"
        self.acl_radio_udp.Text = "UDP"
        self.acl_radio_udp.Location = Point(60, 17)

        self.acl_radio_all = self.new_radio()
        self.acl_radio_all.Name = "acl_radio_all"
        self.acl_radio_all.Text = "All"
        self.acl_radio_all.Location = Point(110, 17)
        self.acl_radio_all.Checked = True

        # Protocol groubox for radio options
        self.acl_groupbox = GroupBox()
        self.acl_groupbox.Location = Point(17, 40)
        self.acl_groupbox.Name = "acl_groupbox"
        self.acl_groupbox.Size = Size(162, 40)
        self.acl_groupbox.Font = Font("Lucida Console", 8)
        self.acl_groupbox.Text = "Protocol"
        self.acl_groupbox.Anchor = AnchorStyles.Top
        # adding items to groupbox
        self.acl_groupbox.Controls.Add(self.acl_radio_tcp)
        self.acl_groupbox.Controls.Add(self.acl_radio_udp)
        self.acl_groupbox.Controls.Add(self.acl_radio_all)

        # Source typeLabel
        self.acl_label_src_type = self.new_label()
        self.acl_label_src_type.Name = "acl_label_src_type"
        self.acl_label_src_type.Location = Point(190, 45)
        self.acl_label_src_type.Size = Size(90, 20)
        self.acl_label_src_type.Font = Font("Lucida Console", 8)
        self.acl_label_src_type.Text = "Source Type:"
        # Source type combo box
        self.acl_box_src_type = self.new_combobox()
        self.acl_box_src_type.Name = "acl_source_type_box"
        self.acl_box_src_type.Items.AddRange(("host", "object-group", "object"))
        self.acl_box_src_type.Text = "object-group"
        self.acl_box_src_type.Location = Point(281, 40)
        # Dest type lable
        self.acl_label_dest_type = self.new_label()
        self.acl_label_dest_type.Name = "acl_label_dest_type"
        self.acl_label_dest_type.Location = Point(192, 71)
        self.acl_label_dest_type.Size = Size(90, 20)
        self.acl_label_dest_type.Font = Font("Lucida Console", 8)
        self.acl_label_dest_type.Text = "Dest. Type:"
        # Dest type combo box
        self.acl_box_dest_type = self.new_combobox()
        self.acl_box_dest_type.Name = "acl_box_dest_type"
        self.acl_box_dest_type.Items.AddRange(("host", "object-group", "object"))
        self.acl_box_dest_type.Text = "object-group"
        self.acl_box_dest_type.Location = Point(281, 66)

        # source text entry
        self.acl_entry_src = self.new_textbox()
        self.acl_entry_src.Name = "acl_entry_src"
        self.acl_entry_src.Size = Size(384, 20)
        self.acl_entry_src.Location = Point(17, 98)
        self.acl_entry_src.Text = "source-object-group"
        # destination text entry
        self.acl_entry_dest = self.new_textbox()
        self.acl_entry_dest.Name = "acl_dest_name"
        self.acl_entry_dest.Size = Size(384, 20)
        self.acl_entry_dest.Location = Point(17, 120)
        self.acl_entry_dest.Text = "destination-object-group"

        self.acl_box_port = self.new_combobox()
        self.acl_box_port.Name = "acl_proto_box"
        self.acl_box_port.Items.AddRange(("port", "object-group", "object"))
        self.acl_box_port.Text = "object-group"
        self.acl_box_port.Location = Point(85, 140)

        self.acl_label_port = self.new_label()
        self.acl_label_port.Anchor = AnchorStyles.Top
        self.acl_label_port.Text = "Port Type:"
        self.acl_label_port.Size = Size(120, 30)
        self.acl_label_port.Size = Size(80, 20)
        self.acl_label_port.Font = Font("Lucida Console", 9)
        self.acl_label_port.Location = Point(7, 145)

        self.acl_entry_port = self.new_textbox()
        self.acl_entry_port.Name = "acl_proto_field"
        self.acl_entry_port.Size = Size(190, 20)
        self.acl_entry_port.Location = Point(211, 141)

        self.acl_btn_print = self.new_button()
        self.acl_btn_print.Location = Point(17, 176)
        self.acl_btn_print.Size = Size(384, 40)
        self.acl_btn_print.Text = "Print to Console!"
        self.acl_btn_print.Click += self.acl_print_con

        # ACL panel layout
        self.acl.Controls.Add(self.acl_groupbox)
        self.acl.Controls.Add(self.acl_label)
        self.acl.Controls.Add(self.acl_field_name)
        self.acl.Controls.Add(self.acl_label_src_type)
        self.acl.Controls.Add(self.acl_label_dest_type)
        self.acl.Controls.Add(self.acl_box_src_type)
        self.acl.Controls.Add(self.acl_box_dest_type)
        self.acl.Controls.Add(self.acl_entry_src)
        self.acl.Controls.Add(self.acl_entry_dest)
        self.acl.Controls.Add(self.acl_entry_port)
        self.acl.Controls.Add(self.acl_label_port)
        self.acl.Controls.Add(self.acl_box_port)
        self.acl.Controls.Add(self.acl_entry_port)
        self.acl.Controls.Add(self.acl_btn_print)

        return self.acl



    def activate_tool_4(self, sender, args):
        self.disable_all(self.tool_4_panel.Name)
        self.tool_4_panel.Visible = not self.tool_4_panel.Visible
        self.tool_4_panel.Enabled = self.tool_4_panel.Visible
        if self.tool_4_panel.Enabled is True:
            self.button_tool_4.BackColor = self.color_button_sel
        else:
            self.button_tool_4.BackColor = self.color_button
        return

    def new_label(self):
        label = Label()
        label.BackColor = Color.Transparent
        label.Font = Font("Lucida Console", 10)
        label.Anchor = AnchorStyles.Top
        return label

    def new_button(self):
        button = Button()
        button.BackColor = self.color_button
        button.Anchor = AnchorStyles.Top
        button.Text = "Button"
        button.Font = Font("Lucida Console", 10, FontStyle.Bold)
        button.Size = Size(92, 32)
        return button

    def new_radio(self):
        radio = RadioButton()
        radio.Font = Font("Lucida Console", 10)
        radio.ForeColor = self.color_window
        radio.Size = Size(50, 15)
        return radio

    def new_combobox(self):
        combobox = ComboBox()
        combobox.Font = Font("Lucida Console", 8)
        combobox.BackColor = self.color_window
        combobox.ForeColor = self.color_title
        combobox.Anchor = AnchorStyles.Top
        combobox.Size = Size(120, 21)
        return combobox

    def new_textbox(self):
        textbox = TextBox()
        textbox.Font = Font("Lucida Console", 8)
        textbox.BackColor = self.color_window
        textbox.ForeColor = self.color_title
        textbox.Anchor = AnchorStyles.Top
        textbox.TextAlign = HorizontalAlignment.Center
        return textbox

    def new_panel(self):
        panel = Panel()
        panel.Size = Size(420, 260)
        panel.Location = Point(30, 75)
        panel.BackColor = self.color_panel
        panel.Anchor = (AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top)
        panel.Visible = False
        panel.Enabled = panel.Visible
        return panel

    # ACL TOOL PRINTER
    def acl_print_con(self, sender, args):
        acl_name = self.acl_label.Text
        protocol = [self.acl_radio_tcp.Checked, self.acl_radio_udp.Checked,
                    self.acl_radio_all.Checked]
        if protocol[0]:
            protocol = "tcp"
        elif protocol[1]:
            protocol = "udp"
        elif protocol[2]:
            protocol = "ip"
        dest_type = self.acl_box_dest_type.Text
        source_type = self.acl_box_src_type.Text

        dest = self.acl_entry_dest.Text
        source = self.acl_entry_src.Text
        port_type = self.acl_box_port.Text
        port = self.acl_entry_port.Text

        submission = ["access-list", acl_name, protocol, source_type, source, dest_type, dest]

        if protocol != "ip":
            submission.append(port_type)
            submission.append(port)

        submission = " ".join(submission)
        self.console_write(submission)
        self.console_box.Focus()
        self.Width = 1000
        self.console_box.SelectionStart = self.console_box.TextLength
        self.console_box.ScrollToCaret()

        # Tool activator 2

    def placeholder_tool_1(self, sender, args):
        self.disable_all(self.placeholder_panel_1.Name)
        self.placeholder_panel_1.Visible = not self.placeholder_panel_1.Visible
        self.placeholder_panel_1.Enabled = self.placeholder_panel_1.Visible
        if self.placeholder_panel_1.Enabled is True:
            self.button_ph_tool_1.BackColor = self.color_button_sel
        else:
            self.button_ph_tool_1.BackColor = self.color_button
        return

    # Tool activator 1
    def acl_tool(self, sender, args):
        self.disable_all(self.acl_panel_new.Name)
        self.acl_panel_new.Visible = not self.acl_panel_new.Visible
        self.acl_panel_new.Enabled = self.acl_panel_new.Visible
        if self.acl_panel_new.Enabled is True:
            self.button_acl_tool.BackColor = self.color_button_sel
        else:
            self.button_acl_tool.BackColor = self.color_button

    def disable_all(self, own_panel):
        panel_names = [self.acl_panel_new.Name, self.placeholder_panel_1.Name, self.placeholder_panel_2.Name,
                       self.tool_4_panel.Name]
        panels = [self.acl_panel_new, self.placeholder_panel_1, self.placeholder_panel_2, self.tool_4_panel]
        buttons = [self.button_acl_tool, self.button_ph_tool_1, self.button_ph_tool_2, self.button_tool_4]
        # self.dbw("own_panel value", own_panel)
        for panel_name, panel, button in zip(panel_names, panels, buttons):
            if str(own_panel) != str(panel):
                panel.Visible = False
                panel.Enabled = False
                button.BackColor = self.color_button
            if str(own_panel) == str(panel):
                panel.Visible = True
                panel.Enabled == True
                button.BackColor = self.color_button_sel

    def dbw(self, tag, text):
        self.console_box.Text += ' >>> ' + tag + ' : ' + str(text) + ' >>>' + Environment.NewLine

    def console_write(self, text):
        self.console_box.Text += (str(text) + Environment.NewLine)

    def radio_check(self, sender, args):
        self.console_write("Poop")
        return


form = FormOne()
Application.Run(form)
