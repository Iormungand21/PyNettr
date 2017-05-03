import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *
from System import EventHandler, Environment


class FormOne(Form):

    def __init__(self):

        #Colors
        self.color_title = Color.FromArgb(135, 189, 68)
        self.color_button_sel = Color.FromArgb(153, 198, 91)
        self.color_button = Color.FromArgb(103, 148, 41)
        self.color_window = Color.FromArgb(48, 48, 48)
        self.color_panel = Color.FromArgb(124, 124, 124)

        #Window parameters
        self.Text = "PyNettr 0.1.0"
        self.Name = "Test"
        self.Size = Size(500,550)
        self.MinimumSize = Size (460, 480)
        self.BackColor = self.color_window
        self.Icon = Icon("res\\icon.ico")

        #Top Main Label
        self.top_label = Label()
        self.top_label.Anchor = AnchorStyles.Top
        self.top_label.Text = "PyNettr"
        self.top_label.Size = Size(120,30)
        self.top_label.ForeColor = self.color_title
        self.top_label.Font = Font("Lucida Console", 16, FontStyle.Bold)
        self.top_label.Location = Point(185,3)

        #Console box to write to
        self.console_box = TextBox()
        self.console_box.Multiline = True
        self.console_box.ReadOnly = True
        self.console_box.ScrollBars = ScrollBars.Vertical
        self.console_box.Size = Size(420,120)
        self.console_box.Location = Point(30,360)
        self.console_box.Anchor = (AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom )

        #Placeholder_1 Tool panel#################################
        self.placeholder_panel_1 = self.new_panel()
        self.placeholder_panel_1.Name = "placeholder_panel_1"

        #Placeholder_2 Tool Panel##################################
        self.placeholder_panel_2 = self.new_panel()
        self.placeholder_panel_2.Name = "placeholder_panel_2"

        #Placeholder_3 Tool Panel##################################
        self.placeholder_panel_3 = self.new_panel()
        self.placeholder_panel_3.Name = "placeholder_panel_3"

        # ACL Tool Panel########################################
        self.acl_panel = self.new_panel()
        self.acl_panel.Name = "acl_panel"

        #ACL name label
        self.acl_label = Label()
        self.acl_label.Location = Point(14,14)
        self.acl_label.BackColor = Color.Transparent
        self.acl_label.Size = Size(79,15)
        self.acl_label.Text = "ACL Name:"
        self.acl_label.Font = Font("Lucida Console", 10)

        #ACL name field
        self.acl_name_field = self.new_textbox()
        self.acl_name_field.Location = Point(100,11)
        self.acl_name_field.Size = Size(300,20)
        self.acl_name_field.Text = "Outside_access_in"

        #Protocol radio buttons
        self.acl_proto_tcp_radio = self.new_radio()
        self.acl_proto_tcp_radio.Name = "acl_proto_tcp_radio"
        self.acl_proto_tcp_radio.Text = "TCP"
        self.acl_proto_tcp_radio.Location = Point(10,17)

        self.acl_proto_udp_radio = self.new_radio()
        self.acl_proto_udp_radio.Name = "acl_proto_udp_radio"
        self.acl_proto_udp_radio.Text = "UDP"
        self.acl_proto_udp_radio.Location = Point(60,17)

        self.acl_proto_all_radio = self.new_radio()
        self.acl_proto_all_radio.Name = "acl_proto_all_radio"
        self.acl_proto_all_radio.Text = "All"
        self.acl_proto_all_radio.Location = Point(110,17)
        self.acl_proto_all_radio.Checked = True



        #Protocol groubox for radio options
        self.acl_proto_groupbox = GroupBox()
        self.acl_proto_groupbox.Location = Point(17, 36)
        self.acl_proto_groupbox.Name = "acl_proto_groupbox"
        self.acl_proto_groupbox.Size = Size (162, 40)
        self.acl_proto_groupbox.Font = Font("Lucida Console", 8)
        self.acl_proto_groupbox.Text = "Protocol"
        #adding items to groupbox
        self.acl_proto_groupbox.Controls.Add(self.acl_proto_tcp_radio)
        self.acl_proto_groupbox.Controls.Add(self.acl_proto_udp_radio)
        self.acl_proto_groupbox.Controls.Add(self.acl_proto_all_radio)
       
        # Source typeLabel
        self.acl_source_type_label = Label()
        self.acl_source_type_label.Name = "acl_source_type_label"
        self.acl_source_type_label.Location = Point(190,45)
        self.acl_source_type_label.Font = Font("Lucida Console", 8)
        self.acl_source_type_label.Text = "Source Type:"
        #Source type combo box
        self.acl_source_type_box = self.new_combobox()
        self.acl_source_type_box.Name = "acl_source_type_box"
        self.acl_source_type_box.Items.AddRange(("host", "object-group", "object"))
        self.acl_source_type_box.Text = "object-group"
        self.acl_source_type_box.Location = Point(281, 40)
        # Dest type lable
        self.acl_dest_type_label = Label()
        self.acl_dest_type_label.Name = "acl_dest_type_label"
        self.acl_dest_type_label.Location = Point(192,71)
        self.acl_dest_type_label.Font = Font("Lucida Console", 8)
        self.acl_dest_type_label.Text = "Dest. Type:"
        #Dest type combo box
        self.acl_dest_type_box = self.new_combobox()
        self.acl_dest_type_box.Name = "acl_dest_type_box"
        self.acl_dest_type_box.Items.AddRange(("host", "object-group", "object"))
        self.acl_dest_type_box.Text = "object-group"
        self.acl_dest_type_box.Location = Point(281, 66)

        #source text entry
        self.acl_source_entry = self.new_textbox()
        self.acl_source_entry.Name = "acl_source_entry"
        self.acl_source_entry.Size = Size(384, 20)
        self.acl_source_entry.Location = Point(17, 98)
        self.acl_source_entry.Text = "source-object-group"
        #destination text entry
        self.acl_dest_entry = self.new_textbox()
        self.acl_dest_entry.Name = "acl_dest_name"
        self.acl_dest_entry.Size = Size(384, 20)
        self.acl_dest_entry.Location = Point(17, 120)
        self.acl_dest_entry.Text = "destination-object-group"

        self.acl_port_box = self.new_combobox()
        self.acl_port_box.Name = "acl_proto_box"
        self.acl_port_box.Items.AddRange(("port", "object-group", "object"))
        self.acl_port_box.Text = "object-group"
        self.acl_port_box.Location = Point(85,140)
        
        self.acl_port_label = Label()
        self.acl_port_label.Anchor = AnchorStyles.Top
        self.acl_port_label.Text = "Port Type:"
        self.acl_port_label.Size = Size(120,30)
        self.acl_port_label.Font = Font("Lucida Console", 9)
        self.acl_port_label.Location = Point(7,145)

        self.acl_port_entry = self.new_textbox()
        self.acl_port_entry.Name = "acl_proto_field"
        self.acl_port_entry.Size = Size(190, 20)
        self.acl_port_entry.Location = Point(211, 141)

        self.acl_print_btn = self.new_button()
        self.acl_print_btn.Location = Point(17, 176)
        self.acl_print_btn.Size = Size(384, 40)
        self.acl_print_btn.Text = "Print to Console!"
        self.acl_print_btn.Click += self.acl_print_con
        



        #ACL panel layout
        self.acl_panel.Controls.Add(self.acl_label)
        self.acl_panel.Controls.Add(self.acl_name_field)
        self.acl_panel.Controls.Add(self.acl_proto_groupbox)
        self.acl_panel.Controls.Add(self.acl_source_type_box)
        self.acl_panel.Controls.Add(self.acl_source_type_label)
        self.acl_panel.Controls.Add(self.acl_dest_type_box)
        self.acl_panel.Controls.Add(self.acl_dest_type_label)
        self.acl_panel.Controls.Add(self.acl_source_entry)
        self.acl_panel.Controls.Add(self.acl_dest_entry)
        self.acl_panel.Controls.Add(self.acl_port_box)
        self.acl_panel.Controls.Add(self.acl_port_label)
        self.acl_panel.Controls.Add(self.acl_port_entry)
        self.acl_panel.Controls.Add(self.acl_print_btn)

        #End of ACL Tool Panel##################################
   

        #Main Tool Buttons######################################
        #Button to activate ACL tool panel
        self.button_acl_tool = self.new_button()
        self.button_acl_tool.Text = "ACL Tool"
        self.button_acl_tool.Location = Point(30,37)
        self.button_acl_tool.Click += self.acl_tool

        #Button to activate X tool panel
        self.button_ph_tool_1 = self.new_button()
        self.button_ph_tool_1.Text = "Test"
        self.button_ph_tool_1.Location = Point(138,37)
        self.button_ph_tool_1.Click += self.placeholder_tool_1

        #Button for phtool2
        self.button_ph_tool_2 = self.new_button()
        self.button_ph_tool_2.Location = Point(247, 37)
        self.button_ph_tool_2.Text ="Test2"
        self.button_ph_tool_2.Click += self.placeholder_tool_2

        #Button for phtool3
        self.button_ph_tool_3 = self.new_button()
        self.button_ph_tool_3.Location = Point(358, 37)
        self.button_ph_tool_3.Text ="Test3"

        #Adding initial layout##################################
        self.Controls.Add(self.top_label)
        #buttons
        self.Controls.Add(self.button_acl_tool)
        self.Controls.Add(self.button_ph_tool_1)
        self.Controls.Add(self.button_ph_tool_2)
        self.Controls.Add(self.button_ph_tool_3)
        #panels
        self.Controls.Add(self.acl_panel)
        self.Controls.Add(self.placeholder_panel_1)
        self.Controls.Add(self.placeholder_panel_2)
        #self.panel_setup_test()

        #debug box
        self.Controls.Add(self.console_box)

    def new_button(self):
        button = Button()
        button.BackColor = self.color_button
        button.Anchor = (AnchorStyles.Top )
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
        combobox.Size = Size(120,21)
        return combobox

    def new_textbox(self):
        textbox = TextBox()
        textbox.Font = Font("Lucida Console", 8)
        textbox.BackColor = self.color_window
        textbox.ForeColor = self.color_title
        textbox.TextAlign = HorizontalAlignment.Center
        return textbox


    def new_panel(self):
        panel = Panel()
        panel.Size = Size(420,260)
        panel.Location = Point(30,75)
        panel.BackColor = self.color_panel
        panel.Anchor = (AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top)
        panel.Visible = False
        panel.Enabled = panel.Visible
        return panel


    #ACL TOOL PRINTER
    def acl_print_con(self, sender, args):
        acl_name = self.acl_name_field.Text
        protocol = [self.acl_proto_tcp_radio.Checked, self.acl_proto_udp_radio.Checked, self.acl_proto_all_radio.Checked]
        if protocol[0]:
            protocol = "tcp"
        elif protocol[1]:
            protocol = "udp"
        elif protocol[2]:
            protocol = "ip"
        dest_type = self.acl_dest_type_box.Text
        source_type = self.acl_source_type_box.Text

        dest = self.acl_dest_entry.Text
        source = self.acl_source_entry.Text
        port_type = self.acl_port_box.Text
        port = self.acl_port_entry.Text

        submission = ["access-list", acl_name, protocol, source_type, source, dest_type, dest]

        if protocol != "ip" :
            submission.append(port_type)
            submission.append(port)

        submission = " ".join(submission)
        self.console_write(submission)
        self.console_box.Focus()
        self.console_box.SelectionStart = self.console_box.TextLength
        self.console_box.ScrollToCaret()

   #Tool activator 2
    def placeholder_tool_1(self, sender, args):
        self.disable_all(self.placeholder_panel_1.Name)
        self.placeholder_panel_1.Visible = not self.placeholder_panel_1.Visible
        self.placeholder_panel_1.Enabled = self.placeholder_panel_1.Visible
        if self.placeholder_panel_1.Enabled is True:
            self.button_ph_tool_1.BackColor = self.color_button_sel
        else:
            self.button_ph_tool_1.BackColor = self.color_button
        return

    #Tool activator 3
    def placeholder_tool_2(self, sender, args):
        self.disable_all(self.placeholder_panel_2.Name)
        #self.dbw("Placeholder button color" , self.button_ph_tool_2.BackColor)
        self.placeholder_panel_2.Visible = not self.placeholder_panel_2.Visible
        self.placeholder_panel_2.Enabled = self.placeholder_panel_2.Visible
        if self.placeholder_panel_2.Enabled is True:
            self.button_ph_tool_2.BackColor = self.color_button_sel
        else:
            self.button_ph_tool_2.BackColor = self.color_button
        return

    #Tool activator 4


    #Tool activator 1
    def acl_tool(self, sender, args):
        self.disable_all(self.acl_panel.Name)
        self.acl_panel.Visible = not self.acl_panel.Visible
        self.acl_panel.Enabled = self.acl_panel.Visible
        if self.acl_panel.Enabled is True:
            self.button_acl_tool.BackColor = self.color_button_sel
        else:
            self.button_acl_tool.BackColor = self.color_button

    def disable_all(self, own_panel):
        panel_names = [self.acl_panel.Name, self.placeholder_panel_1.Name, self.placeholder_panel_2.Name]
        panels = [self.acl_panel, self.placeholder_panel_1, self.placeholder_panel_2]
        buttons = [self.button_acl_tool, self.button_ph_tool_1, self.button_ph_tool_2, self.button_ph_tool_3]
        #self.dbw("own_panel value", own_panel)
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

       