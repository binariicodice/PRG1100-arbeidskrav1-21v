from tkinter import *
from tkinter import ttk

# Python kode for beregning av billån:
def beregne_billan():
    ek = int(egenkapital.get())
    ksum = int(kjopesum.get())
    ntid = int(nedbetalingstid.get())

    positivt_svar = 'Lån innvilges'
    negativt_svar = 'Lån innvilges ikke'
    ek_i_prosent = ek / ksum * 100

    if ek_i_prosent < 35:
        lanetilsagn.set(negativt_svar)
        lanesum_totalt.set('XXXXXX')
        belaningsgrad.set('XXX')
        terminbelop.set('XXXX')
    elif ek_i_prosent >= 35 and ek_i_prosent <= 49:
        arlig_rente = 0.045
        lanetilsagn.set(positivt_svar)
    elif ek_i_prosent >= 50 and ek_i_prosent <= 59:
        arlig_rente = 0.030
        lanetilsagn.set(positivt_svar)
    elif ek_i_prosent >= 60 and ek_i_prosent <= 99.9:
        arlig_rente = 0.025
        lanetilsagn.set(positivt_svar)
    else:
        lanetilsagn.set(negativt_svar)
        lanesum_totalt.set('XXXXXX')
        belaningsgrad.set('XXX')
        terminbelop.set('XXXX')
    # Finne størrelse på egenkapitalen.
    lanesum_totalt_resultat = ksum - ek
    belaningsgrad_resultat = 100 - ek_i_prosent
    # Utregning av termin rente:
    termin_rente = arlig_rente / 12
    # Utregning av antall terminer:
    antall_terminer = ntid * 12
    # Utregning av termin beløper:
    terminbelop_resultat = lanesum_totalt_resultat * (((1 + termin_rente) ** antall_terminer) * termin_rente) / (((1 + termin_rente) ** antall_terminer) - 1)
    # Utregning av lånesum totalt og belåningsgrad.
    lanesum_totalt.set(format(lanesum_totalt_resultat, '.0f'))
    belaningsgrad.set(format(belaningsgrad_resultat, '.1f'))
    terminbelop.set(str(format(terminbelop_resultat, '.0f')))
# GUI for billånkalkulator.
window = Tk()
window.resizable(FALSE, FALSE)
window.title('Lånekalkulator billån')

overskrift_config = Text(window, height=5, width=50)
overskrift = Label(window, text='Billånskalkulator')
overskrift.grid(row=0, columnspan=2)
overskrift.configure(font=("Sans-Serif", 20))

under_overskrift_config = Text(window, height=5, width=50)
under_overskrift = Label(window, text="* Krav om 35% i egenkapital")
under_overskrift.grid(row=1, columnspan=2)

lbl_kjopesum = Label(window, text='Kjøpesum:')
lbl_kjopesum.grid(row=2, column=0, padx=10, pady=5, sticky=E)

lbl_kjopesum_txt = Label(window, text='kr')
lbl_kjopesum_txt.grid(row=2, column=1, padx=55, pady=5, sticky=W)

lbl_egenkapital = Label(window, text='Egenkapital:')
lbl_egenkapital.grid(row=4, column=0, padx=10, pady=5, sticky=E)

lbl_egenkapital_txt = Label(window, text='kr')
lbl_egenkapital_txt.grid(row=4, column=1, padx=55, pady=5, sticky=W)

lbl_nedbetalingstid = Label(window, text='Nedbetalingstid:')
lbl_nedbetalingstid.grid(row=6, column=0, padx=10, pady=5, sticky=E)

lbl_nedbetalingstid_txt = Label(window, text='år')
lbl_nedbetalingstid_txt.grid(row=6, column=1, padx=25, pady=5, sticky=W)

btn_beregn = Button(window,text='Beregn lånetilsagn', command=beregne_billan) 
btn_beregn.grid(row=8, column=1, padx=10, pady=5, sticky=W)

lbl_lanetilsagn = Label(window, text='Lånetilsagn:')
lbl_lanetilsagn.grid(row=9, column=0, padx=10, pady=5, sticky=E)

lbl_lanesum_totalt = Label(window, text='Lånesum totalt:')
lbl_lanesum_totalt.grid(row=10, column=0, padx=10, pady=5, sticky=E)

lbl_belaningsgrad = Label(window, text='Belåningsgrad:')
lbl_belaningsgrad.grid(row=11, column=0, padx=10, pady=5, sticky=E)

lbl_terminbelop = Label(window, text='Terminbeløp:')
lbl_terminbelop.grid(row=12, column=0, padx=10, pady=5, sticky=E)

kjopesum = StringVar()
ent_kjopesum = Entry(window, width=7, textvariable=kjopesum)
ent_kjopesum.grid(row=2, column=1, padx=5, pady=5, sticky=W)
ent_kjopesum_scale = ttk.Scale(window, orient=HORIZONTAL, length=150, from_=1, to=2000000, variable=kjopesum, command=lambda s:kjopesum.set('%0.0f' % float(s)))
ent_kjopesum_scale.grid(row=3, columnspan=2, pady=5)
ent_egenkapital_scale = ttk.Label(text="test", style=".TFrame")

egenkapital = StringVar()
ent_egenkapital = Entry(window, width=7, textvariable=egenkapital)
ent_egenkapital.grid(row=4, column=1, padx=5, pady=5, sticky=W)
ent_egenkapital_scale = ttk.Scale(window, orient=HORIZONTAL, length=150, from_=1, to=2000000, variable=egenkapital, command=lambda s:egenkapital.set('%0.0f' % float(s)))
ent_egenkapital_scale.grid(row=5, columnspan=2, pady=5)

nedbetalingstid = StringVar()
ent_nedbetalingstid = Entry(window, width=2, textvariable=nedbetalingstid)
ent_nedbetalingstid.grid(row=6, column=1, padx=5, pady=5, sticky=W)
ent_nedbetalingstid_scale = ttk.Scale(window, orient=HORIZONTAL, length=150, from_=1, to=10, variable=nedbetalingstid, command=lambda s:nedbetalingstid.set('%0.0f' % float(s)))
ent_nedbetalingstid_scale.grid(row=7, columnspan=2, pady=5)

lanetilsagn = StringVar()
ent_lanetilsagn = Entry(window, width=18, state='readonly', textvariable=lanetilsagn)
ent_lanetilsagn.grid(row=9, column=1, padx=5, pady=5, sticky=W)

lanesum_totalt = StringVar()
ent_lanesum_totalt = Entry(window, width=7, state='readonly', textvariable=lanesum_totalt)
ent_lanesum_totalt.grid(row=10, column=1, padx=5, pady=5, sticky=W)

lbl_lanesum_totalt_txt = Label(window, text='kr')
lbl_lanesum_totalt_txt.grid(row=10, column=1, padx=55, pady=5, sticky=W)

belaningsgrad = StringVar()
ent_belaningsgrad = Entry(window, width=4, state='readonly', textvariable=belaningsgrad)
ent_belaningsgrad.grid(row=11, column=1, padx=5, pady=5, sticky=W)

lbl_belaningsgrad_txt = Label(window, text='%')
lbl_belaningsgrad_txt.grid(row=11, column=1, padx=35, pady=5, sticky=W)

terminbelop = StringVar()
ent_terminbelop = Entry(window, width=5, state='readonly', textvariable=terminbelop)
ent_terminbelop.grid(row=12, column=1, padx=5, pady=5, sticky=W)

lbl_terminbelop_txt = Label(window, text='kr')
lbl_terminbelop_txt.grid(row=12, column=1, padx=42, pady=5, sticky=W)

btn_avslutt = Button(window,text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=13, column=1, padx=10, pady=12, sticky=E)

window.mainloop()