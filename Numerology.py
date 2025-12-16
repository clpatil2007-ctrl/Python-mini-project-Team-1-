from tkinter import *
from tkinter import messagebox
import csv

global Mobno0
global Date
global Month0
global Year0
def Num_main():


    root = Tk()
    root.configure(bg='cyan4')
    root.title('Numerology')
    root.geometry('1366x768')


    def page1():
        Mobno0 = entry1.get()  # string
        Date0 = entry2.get()  # string
        Month0 = entry3.get()  # string
        Year0 = entry4.get()  # string
        try:
            Mobno = int(Mobno0)  # integer datatype
        except ValueError:
            messagebox.showinfo('NEXT', 'Input the Mob No in integer')
        try:
            Date = int(Date0)  # integer datatype
        except ValueError:
            messagebox.showinfo('NEXT', 'Input the Date in integer')
        try:
            Month = int(Month0)  # integer datatype
        except ValueError:
            messagebox.showinfo('NEXT', 'Input the Month in integer')
        try:
            Year = int(Year0)  # integer datatype
        except ValueError:
            messagebox.showinfo('NEXT', 'Input the Year in integer')

        if Date <= 31 and Month <= 12 and Year <= 9999 and len(Mobno0) == 10 and Date > 0 and Month > 0 and Year > 999:
            f = open("Numerology.txt", 'a')
            b = csv.writer(f)
            global l
            l = [Mobno0, Date, Month, Year]
            b.writerow(l)
            f.close()
            n = (Year // 1000) + ((Year % 1000) // 100) + ((Year % 100) // 10) + (Year % 10) + (Month // 10) + (
                        Month % 10) + (Date // 10) + (Date % 10)
            sum1 = 0  # numerological number if n>9 and n if n<9
            sum2 = 0  # numerological number if sum1>9

            if n > 9:
                while n > 0:
                    sum1 = sum1 + n % 10
                    n = n // 10
                if sum1 > 9:
                    while sum1 > 0:
                        sum2 = sum2 + sum1 % 10  # numerological number =4=max
                        sum1 = sum1 // 10
                    if sum2 == 1:  # sum2=1 to 4

                        top1 = Tk()
                        top1.configure(bg='yellow')
                        top1.title('Numerology')
                        top1.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text1 = '''Hello customer,your number is 1.Here are some pros and cons about you:
    
    STRENGTHS:
    You are a natural leader,creative and hard working.
    You can be known for being self dependent,powerful and ambitious.
    
    WEAKNESS:
    You can be egoistic,stubborn and dominating.
    You can be impatient and their independence can lead to isolation.
    
    LUCKY NUMBERS: 1,2,4,7
    
    LUCKY COLOURS: gold,brown,yellow and orange.
    
    CAREER PATHS: will be good in sports,tech,engineering,etc.'''
                        label9 = Label(top1, text=text1, bg='yellow', fg='black', font=('Areal', 25))
                        label9.place(x=5, y=5)

                    elif sum2 == 2:

                        top1 = Tk()
                        top1.configure(bg='magenta')
                        top1.title('Numerology')
                        top1.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text1 = '''Hello customer,your number is 2.Here are some pros and cons about you:
    STRENGTHS:
    You are diplomatic,adaptable,and often good at conflict resolution
    you are said to be empathetic,harmonious,good at teamwork.
    
    WEAKNESS:
    You can be oversensitive,which can hurt relationships.
    You could struggle with indecisiveness,difficulty with saying no.
    
    LUCKY NUMBERS: 1,3,5,2
    
    LUCKY COLOURS: white,green,yellow,silver,pink,blue.
    
    CAREER PATHS: will be good in public speaking,healers,counselors,etc.'''
                        label9 = Label(top1, text=text1, bg='magenta', fg='black', font=('Areal', 25))
                        label9.place(x=5, y=5)

                    elif sum2 == 3:

                        top1 = Tk()
                        top1.configure(bg='orange')
                        top1.title('Numerology')
                        top1.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text1 = '''Hello customer,your number is 3.Here are some pros and cons about you:
    STRENGTHS:
    You are creative,charismatic, and have positive outlook.
    You are said to be natural solvers,think outside the box.
    
    WEAKNESS:
    You can be scattered,difficulty in focussing on one thing.
    You could make hasty decisions,tendency to overindulge.
    
    LUCKY NUMBERS: 1,2,3,5.
    
    LUCKY COLOURS: yellow,orange and pink.
    
    CAREER PATHS:Which involve creativity,communication,self-expression.'''
                        label9 = Label(top1, text=text1, bg='orange', fg='black', font=('Areal', 25))
                        label9.place(x=5, y=5)

                    elif sum2 == 4:

                        top1 = Tk()
                        top1.configure(bg='green')
                        top1.title('Numerology')
                        top1.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text1 = '''Hello customer,your number is 4.Here are some pros and cons about you:
    STRENGTHS:
    You are known for being punctual and consistant.
    You are said to be practical,reliable and disciplined.
    
    WEAKNESS:
    You can be scattered,difficulty in focussing on one thing.
    You could make hasty decisions,tendency to overindulge.
    
    LUCKY NUMBERS: 1,5,6,7.
    
    LUCKY COLOURS: blue,green,red.
    
    CAREER PATHS:Finance,law,accounting,engineering,science,etc.'''
                        label9 = Label(top1, text=text1, bg='green', fg='black', font=('Areal', 25))
                        label9.place(x=5, y=5)

                if sum1 <= 9:  # sum1=1 to 9
                    if sum1 == 1:

                        top2 = Tk()
                        top2.configure(bg='yellow')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 1.Here are some pros and cons about you:
    
    STRENGTHS:
    You are a natural leader,creative and hard working.
    You can be known for being self dependent,powerful and ambitious.
    
    WEAKNESS:
    You can be egoistic,stubborn and dominating.
    You can be impatient and their independence can lead to isolation.
    
    LUCKY NUMBERS: 1,2,4,7
    
    LUCKY COLOURS: gold,brown,yellow and orange.
    
    CARREER PATHS: will be good in sports,tech,engineering,etc.'''
                        label10 = Label(top2, text=text2, bg='yellow', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


                    elif sum1 == 2:

                        top2 = Tk()
                        top2.configure(bg='magenta')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 2.Here are some pros and cons about you:
    STRENGTHS:
    You are diplomatic,adaptable,and often good at conflict resolution
    You are said to be empathetic,harmonious,good at teamwork.
    
    WEAKNESS:
    You can be oversensitive,which can hurt relationships.
    You could struggle with indecisiveness,difficulty with saying no.
    
    LUCKY NUMBERS: 1,3,5,2
    
    LUCKY COLOURS: white,green,yellow,silver,pink,blue.
    
    CAREER PATHS: will be good in public speaking,healers,counselors,etc.'''
                        label10 = Label(top2, text=text2, bg='magenta', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


                    elif sum1 == 3:

                        top2 = Tk()
                        top2.configure(bg='orange')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 3.Here are some pros and cons about you:
    STRENGTHS:
    You are creative,charismatic, and have positive outlook.
    You are said to be natural solvers,think outside the box.
    
    WEAKNESS:
    You can be scattered,difficulty in focussing on one thing.
    You could make hasty decisions,tendency to overindulge.
    
    LUCKY NUMBERS: 1,2,3,5.
    
    LUCKY COLOURS: yellow,orange and pink.
    
    CAREER PATHS:Which involve creativity,communication,self-expression.'''
                        label10 = Label(top2, text=text2, bg='orange', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


                    elif sum1 == 4:

                        top2 = Tk()
                        top2.configure(bg='green')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 4.Here are some pros and cons about you:
    STRENGTHS:
    You are known for being punctual and consistant.
    You are said to be practical,reliable and disciplined.
    
    WEAKNESS:
    You can be scattered,difficulty in focussing on one thing.
    You could make hasty decisions,tendency to overindulge.
    
    LUCKY NUMBERS: 1,5,6,7.
    
    LUCKY COLOURS: blue,green,red.
    
    CAREER PATHS:Finance,law,accounting,engineering,science,etc.'''
                        label10 = Label(top2, text=text2, bg='green', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)

                    elif sum1 == 5:

                        top2 = Tk()
                        top2.configure(bg='sky blue')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 5.Here are some pros and cons about you:
    STRENGTHS:
    You are known to adapt and have good communication skills.
    You are said to be intelligent,adventurous,have curiosity.
    
    WEAKNESS:
    You can be impatient,inaccurate and impulsive.
    You may struggle with discipline,indecisiveness and be inconsistent.
    
    LUCKY NUMBERS: 1,2,4,6,8.
    
    LUCKY COLOURS: light blue,green,silver,light brown.
    
    CAREER PATHS:travel,marketing,filmmaking,journalism,sales,etc.'''
                        label10 = Label(top2, text=text2, bg='sky blue', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


                    elif sum1 == 6:

                        top2 = Tk()
                        top2.configure(bg='red')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 6.Here are some pros and cons about you:
    STRENGTHS:
    You are known be gentle,caring,empathetic.
    You are said to be reliable,creative and nurturing.
    
    WEAKNESS:
    You can be self-sacrificing and try to avoid conflict.
    You may have perfectionism,emotional dependence,weak boundaries.
    
    LUCKY NUMBERS: 1,5,6.
    
    LUCKY COLOURS:light blue,red,green.
    
    CAREER PATHS:nursing,teaching,healthcare,community service,etc.'''
                        label10 = Label(top2, text=text2, bg='red', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


                    elif sum1 == 7:

                        top2 = Tk()
                        top2.configure(bg='brown')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 7.Here are some pros and cons about you:
    STRENGTHS:
    You are known for creativity and intuition.
    You are said to be great healers and spiritual gurus.
    
    WEAKNESS:
    Its an unfortunate number.
    You may have anxiety issues and be moody.
    
    LUCKY NUMBERS: 4,5,6,8.
    
    LUCKY COLOURS:green,brown.
    
    CAREER PATHS:Psychologist,lawyer,scientist,researcher,journalist,etc.'''
                        label10 = Label(top2, text=text2, bg='brown', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


                    elif sum1 == 8:

                        top2 = Tk()
                        top2.configure(bg='purple')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 8.Here are some pros and cons about you:
    STRENGTHS:
    You are known for strong ambition, practical skills.
    You are said to be judgemental, determined, leadership qualities.
    
    WEAKNESS:
    You can be stubborn at times, materialistic.
    You may have fear of failing,you might also be a workaholic.
    
    LUCKY NUMBERS: 2,3,5,6.
    
    LUCKY COLOURS:black,dark blue,grey,purple.
    
    CAREER PATHS:Technical department, petrochemical industry, engineering.'''
                        label10 = Label(top2, text=text2, bg='purple', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


                    elif sum1 == 9:

                        top2 = Tk()
                        top2.configure(bg='silver')
                        top2.title('Numerology')
                        top2.geometry('1366x768')
                        entry1.delete(0, 'end')
                        entry2.delete(0, 'end')
                        entry3.delete(0, 'end')
                        entry4.delete(0, 'end')
                        text2 = '''Hello customer,your number is 9.Here are some pros and cons about you:
    STRENGTHS:
    You are known for your flexibility.
    You are said to be open minded, passionate, honest.
    
    WEAKNESS:
    You can make rash decisions and be argumentative.
    You are said to be scattered possessive and reckless with money.
    
    LUCKY NUMBERS:9,6,3,5,1.
    
    LUCKY COLOURS:purple, blue, green, gold, lavender, silver.
    
    CAREER PATHS: Art, photography,politics,librarianship,therapy, and social work.'''
                        label10 = Label(top2, text=text2, bg='silver', fg='black', font=('Areal', 25))
                        label10.place(x=5, y=5)


            else:  # n=1to9

                if n == 1:

                    top3 = Tk()
                    top3.configure(bg='yellow')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 1.Here are some pros and cons about you:
    
    STRENGTHS:
    You are a natural leader,creative and hard working.
    You can be known for being self dependent,powerful and ambitious.
    
    WEAKNESS:
    You can be egoistic,stubborn and dominating.
    You can be impatient and their independence can lead to isolation.
    
    LUCKY NUMBERS: 1,2,4,7
    
    LUCKY COLOURS: gold,brown,yellow and orange.
    
    CAREER PATHS: will be good in sports,tech,engineering,etc.'''
                    label10 = Label(top3, text=text3, bg='yellow', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)


                elif n == 2:

                    top3 = Tk()
                    top3.configure(bg='magenta')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 2.Here are some pros and cons about you:
    STRENGTHS:
    You are diplomatic,adaptable,and often good at conflict resolution
    you are said to be empathetic,harmonious,good at teamwork.
    
    WEAKNESS:
    You can be oversensitive,which can hurt relationships.
    You could struggle with indecisiveness,difficulty with saying no.
    
    LUCKY NUMBERS: 1,3,5,2
    
    LUCKY COLOURS: white,green,yellow,silver,pink,blue.
    
    CAREER PATHS: will be good in public speaking,healers,counselors,etc.'''
                    label10 = Label(top3, text=text3, bg='magenta', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)


                elif n == 3:

                    top3 = Tk()
                    top3.configure(bg='orange')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 3.Here are some pros and cons about you:
    STRENGTHS:
    You are creative,charismatic, and have positive outlook.
    You are said to be natural solvers,think outside the box.
    
    WEAKNESS:
    You can be scattered,difficulty in focussing on one thing.
    You could make hasty decisions,tendency to overindulge.
    
    LUCKY NUMBERS: 1,2,3,5.
    
    LUCKY COLOURS: yellow,orange and pink.
    
    CAREER PATHS:Which involve creativity,communication,self-expression.'''
                    label10 = Label(top3, text=text3, bg='orange', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)


                elif n == 4:

                    top3 = Tk()
                    top3.configure(bg='green')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 4.Here are some pros and cons about you:
    STRENGTHS:
    You are known for being punctual and consistant.
    You are said to be practical,reliable and disciplined.
    
    WEAKNESS:
    You can be scattered,difficulty in focussing on one thing.
    You could make hasty decisions,tendency to overindulge.
    
    LUCKY NUMBERS: 1,5,6,7.
    
    LUCKY COLOURS: blue,green,red.
    
    CAREER PATHS:Finance,law,accounting,engineering,science,etc.'''
                    label10 = Label(top3, text=text3, bg='green', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)


                elif n == 5:

                    top3 = Tk()
                    top3.configure(bg='sky blue')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 5.Here are some pros and cons about you:
    STRENGTHS:
    You are known to adapt and have good communication skills.
    You are said to be intelligent,adventurous,have curiosity.
    
    WEAKNESS:
    You can be impatient,inaccurate and impulsive.
    You may struggle with discipline,indecisiveness and be inconsistent.
    
    LUCKY NUMBERS: 1,2,4,6,8.
    
    LUCKY COLOURS: light blue,green,silver,light brown.
    
    CAREER PATHS:travel,marketing,filmmaking,journalism,sales,etc.'''
                    label10 = Label(top3, text=text3, bg='sky blue', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)



                elif n == 6:

                    top3 = Tk()
                    top3.configure(bg='red')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 6.Here are some pros and cons about you:
    STRENGTHS:
    You are known be gentle,caring,empathetic.
    You are said to be reliable,creative and nurturing.
    
    WEAKNESS:
    You can be self-sacrificing and try to avoid conflict.
    You may have perfectionism,emotional dependence,weak boundaries.
    
    LUCKY NUMBERS: 1,5,6.
    
    LUCKY COLOURS:light blue,red,green.
    
    CAREER PATHS:nursing,teaching,healthcare,community service,etc.'''
                    label10 = Label(top3, text=text3, bg='red', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)


                elif n == 7:

                    top3 = Tk()
                    top3.configure(bg='brown')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 7.Here are some pros and cons about you:
    STRENGTHS:
    You are known for creativity and intuition.
    You are said to be great healers and spiritual gurus.
    
    WEAKNESS:
    Its an unfortunate number.
    You may have anxiety issues and be moody.
    
    LUCKY NUMBERS: 4,5,6,8.
    
    LUCKY COLOURS:green,brown.
    
    CAREER PATHS: Psychologist,lawyer,scientist,researcher,journalist,etc.'''
                    label10 = Label(top3, text=text3, bg='brown', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)

                elif n == 8:

                    top3 = Tk()
                    top3.configure(bg='purple')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 8.Here are some pros and cons about you:
    STRENGTHS:
    You are known for strong ambition, practical skills.
    You are said to be judgemental, determined, leadership qualities.
    
    WEAKNESS:
    You can be stubborn at times, materialistic.
    You may have fear of failing,you might also be a workaholic.
    
    LUCKY NUMBERS: 2,3,5,6.
    
    LUCKY COLOURS:black,dark blue,grey,purple.
    
    CAREER PATHS:Technical department, petrochemical industry, engineering.'''
                    label10 = Label(top3, text=text3, bg='purple', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)

                elif n == 9:

                    top3 = Tk()
                    top3.configure(bg='cyan4')
                    top3.title('Numerology')
                    top3.geometry('1366x768')
                    entry1.delete(0, 'end')
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                    entry4.delete(0, 'end')
                    text3 = '''Hello customer,your number is 9.Here are some pros and cons about you:
    STRENGTHS:
    You are known for your creativeness, flexibility.
    You are said to be open minded, passionate, honest.
    
    WEAKNESS:
    You can make rash decisions and be argumentative.
    You are said to be scattered possessive and reckless with money.
    
    LUCKY NUMBERS:9,6,3,5,1.
    
    LUCKY COLOURS:purple, blue, green, gold, lavender, silver.
    
    CAREER PATHS:Art, photography,politics, librarianship,therapy, and social work.'''
                    label10 = Label(top3, text=text3, bg='cyan4', fg='black', font=('Areal', 25))
                    label10.place(x=5, y=5)

        else:
            messagebox.showinfo('NEXT', 'Input the numbers correctly!')


    label1 = Label(root, text='NUMEROLOGY-KNOW YOURSELF BETTER!', bg='cyan4', fg='pink', font=('Areal', 40))
    label1.place(x=150, y=20)

    label2 = Label(root, text='Enter your Mob No: ', bg='cyan4', fg='black', font=('Areal', 35))
    label2.place(x=50, y=100)

    label3 = Label(root, text='Enter your DOB: ', bg='cyan4', fg='black', font=('Areal', 35))
    label3.place(x=550, y=175)

    label4 = Label(root, text='Date                   : ', bg='cyan4', fg='black', font=('Areal', 35))
    label4.place(x=50, y=250)

    label5 = Label(root, text='Month                 : ', bg='cyan4', fg='black', font=('Areal', 35))
    label5.place(x=50, y=350)

    label6 = Label(root, text='Year                    : ', bg='cyan4', fg='black', font=('Areal', 35))
    label6.place(x=50, y=450)

    entry1 = Entry(root, bd=5, font=('Areal', 30))  # Mob No
    entry1.place(x=500, y=100)

    entry2 = Entry(root, bd=5, font=('Areal', 30))  # day
    entry2.place(x=500, y=250)

    entry3 = Entry(root, bd=5, font=('Areal', 30))  # month
    entry3.place(x=500, y=350)

    entry4 = Entry(root, bd=5, font=('Areal', 30))  # year
    entry4.place(x=500, y=450)

    button1 = Button(root, font=('Areal', 30), bg='cyan3', text='NEXT', bd=5, command=page1)
    button1.place(x=50, y=550)

    root.mainloop()