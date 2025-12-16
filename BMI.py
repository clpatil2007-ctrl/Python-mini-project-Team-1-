import wx
def main():
    import wx

    def calculate_bmi(event):
        try:
            height = float(height_ctrl.GetValue())
            weight = float(weight_ctrl.GetValue())

            if height <= 0:
                raise ValueError("Height must be positive")

            bmi = weight / (height * height)

            if bmi < 18.5:
                category = "Underweight"
                suggestion = "Try increasing calorie intake with nutritious foods and consider strength training."
            elif 18.5 <= bmi < 24.9:
                category = "Normal Weight"
                suggestion = "Maintain your current lifestyle with balanced diet and regular exercise."
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                suggestion = "Consider regular workouts and mindful eating to gradually lower your weight."
            else:
                category = "Obese"
                suggestion = "Focus on a calorie-controlled diet and daily physical activity. Seek guidance if needed."

            message = (
                f"Your BMI is: {bmi:.2f}\n"
                f"Category: {category}\n\n"
                f"Suggestion:\n{suggestion}"
            )

            wx.MessageBox(message, "BMI Result", wx.OK)

        except ValueError:
            wx.MessageBox("⚠️ Please enter valid numeric values.", "Input Error", wx.OK | wx.ICON_WARNING)

    # ---------------- MAIN APP ----------------

    app = wx.App(False)

    frame = wx.Frame(None, title="WxPython BMI Calculator", size=(420, 260))
    panel = wx.Panel(frame)
    panel.SetBackgroundColour("#f0f4ff")  # Soft light blue background

    # ---- TITLE ----
    title = wx.StaticText(panel, label="BMI Calculator")
    title_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
    title.SetFont(title_font)
    title.SetForegroundColour("#1a3d7c")

    # ---- FORM GRID ----
    wrapper = wx.BoxSizer(wx.VERTICAL)
    wrapper.Add(title, flag=wx.ALIGN_CENTER | wx.TOP, border=15)

    sizer = wx.FlexGridSizer(rows=3, cols=2, vgap=8, hgap=10)

    label_font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

    # Height
    ht_label = wx.StaticText(panel, label="Height (meters):")
    ht_label.SetFont(label_font)
    sizer.Add(ht_label)

    height_ctrl = wx.TextCtrl(panel, size=(200, 25))
    sizer.Add(height_ctrl)

    # Weight
    wt_label = wx.StaticText(panel, label="Weight (kg):")
    wt_label.SetFont(label_font)
    sizer.Add(wt_label)

    weight_ctrl = wx.TextCtrl(panel, size=(200, 25))
    sizer.Add(weight_ctrl)

    # Button
    calc_btn = wx.Button(panel, label="Calculate BMI", size=(150, 32))
    calc_btn.SetBackgroundColour("#4a76c9")
    calc_btn.SetForegroundColour("white")
    calc_btn.Bind(wx.EVT_BUTTON, calculate_bmi)

    # Grid placeholder
    sizer.Add((0, 0))
    sizer.Add(calc_btn, flag=wx.TOP, border=5)
    wrapper.Add(sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=20)
    panel.SetSizer(wrapper)
    frame.Centre()
    frame.Show()
    app.MainLoop()