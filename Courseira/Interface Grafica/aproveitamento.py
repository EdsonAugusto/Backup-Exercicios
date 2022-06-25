def aproveitamentoPartidas(par_jogadas,par_perdidas,par_empatas):
    perdidas=((par_jogadas*3)/par_jogadas)*par_perdidas
    empatas=((par_jogadas*3)/par_jogadas)*par_empatas
    media=(par_jogadas*(perdidas+empatas))/par_jogadas
    media2=((par_jogadas*media)/par_jogadas)-par_jogadas*3
    media3=((par_jogadas*3)/par_jogadas)*media2
    return  perdidas, empatas, media, media2,media3
print(aproveitamentoPartidas(5,0,0))