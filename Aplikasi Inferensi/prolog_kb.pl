% =================================================================
% FILE: prolog_kb.pl
% Knowledge Base Logika Orde Pertama (FOL) untuk Analisis Isu Kontemporer
% Topik: Optimasi Urutan Playlist untuk Transisi Mulus Menggunakan Model Graf Berbobot
% =================================================================

% --- TEMA: Optimasi Urutan Playlist untuk Transisi Mulus Menggunakan Model Graf Berbobot ---
% Predikat Utama: lagu, memiliki_atribut, jarak_graf, lagu_ekstrem, pembentuk_outlier, transisi_kasar, butuh_lagu_bridge

% -----------------------------------------------------------------
% 1. DEFINISI FACTS (Minimal 15 Facts / Proposisi Dasar)
%    Format: lagu(Nama).
%            memiliki_atribut(Nama, Genre, Energi, Tempo).
%            jarak_graf(Lagu1, Lagu2, Weight).
% -----------------------------------------------------------------

% --- Fakta 1-5: Definisi Entitas Lagu ---
% Format: lagu(Nama).
lagu(beautiful_world).
lagu(good_luck_babe).
lagu(russian_roulette).
lagu(tripping_wires).
lagu(self_care).

% --- Fakta 6-10: Atribut Lagu (Genre, Energi, Tempo) ---
% Format: memiliki_atribut(Lagu, Genre, Energi, Tempo)
memiliki_atribut(beautiful_world, shoegaze, tinggi, sedang).
memiliki_atribut(good_luck_babe, pop, tinggi, cepat).
memiliki_atribut(russian_roulette, electronic, tinggi, cepat).
memiliki_atribut(self_care, hip_hop, sedang, sedang).
memiliki_atribut(tripping_wires, metal, sangat_tinggi, cepat).

% --- Fakta 11-15: Jarak Graf (Bobot Ketidakmiripan) ---
% Semakin tinggi nilai, semakin tidak cocok (jauh)
% Format: jarak_graf(Lagu1, Lagu2, Weight)
jarak_graf(tripping_wires, self_care, 0.95).
jarak_graf(tripping_wires, good_luck_babe, 0.8).
jarak_graf(good_luck_babe, russian_roulette, 0.2).
jarak_graf(beautiful_world, russian_roulette, 0.6).
jarak_graf(self_care, good_luck_babe, 0.45).


% -----------------------------------------------------------------
% 2. DEFINISI RULES (Minimal 8 Rules / Implikasi FOL)
%    Variabel diawali huruf KAPITAL (X, Y, N).
% -----------------------------------------------------------------

% --- BAGIAN 1: RANTAI INFERENSI 3 LANGKAH (Analisis Outlier/Node) ---

% Rule 1 (Premis 1): Identifikasi Lagu Ekstrem
% FOL: ∀X ((energi(X,sangat_tinggi) ∨ energi(X,rendah)) → lagu_ekstrem(X))
lagu_ekstrem(X) :-
    memiliki_atribut(X, _, sangat_tinggi, _) ;
    memiliki_atribut(X, _, rendah, _).

% Rule 2 (Premis 2): Lagu ekstrem berpotensi menjadi outlier
% FOL: ∀X (lagu_ekstrem(X) → pembentuk_outlier(X))
pembentuk_outlier(X) :-
    lagu_ekstrem(X).

% Rule 3 (Premis 3): Outlier wajib dikurasi manual (tidak boleh auto-shuffle)
% FOL: ∀X (pembentuk_outlier(X) → wajib_kurasi_manual(X))
wajib_kurasi_manual(X) :-
    pembentuk_outlier(X).


% --- BAGIAN 2: LOGIKA HUBUNGAN ANTAR LAGU (Analisis Edge/Transisi) ---

% Rule 4: Pengecekan Beda Genre
% FOL: ∀X,Y (genre(X) ≠ genre(Y) → beda_genre(X,Y))
beda_genre(X, Y) :-
    memiliki_atribut(X, Genre1, _, _),
    memiliki_atribut(Y, Genre2, _, _),
    Genre1 \= Genre2.

% Rule 5: Energi Kontras (Aturan Khusus)
% Jika X sangat tinggi, dan Y sedang atau rendah -> Kontras
% FOL: ∀X,Y (sangat_tinggi(X) ∧ (sedang(Y) ∨ rendah(Y)) → energi_kontras(X,Y))
energi_kontras(X, Y) :-
    memiliki_atribut(X, _, sangat_tinggi, _),
    (
        memiliki_atribut(Y, _, sedang, _) ;
        memiliki_atribut(Y, _, rendah, _)
    ).

% Rule 6: Transisi Kasar (Penyebab utama butuh bridge)
% Terjadi jika energi kontras ATAU jarak graf > 0.7
% FOL: ∀X,Y (energi_kontras(X,Y) ∨ (jarak(X,Y) > 0.7) → transisi_kasar(X,Y))
transisi_kasar(X, Y) :-
    energi_kontras(X, Y) ;
    (jarak_graf(X, Y, Jarak), Jarak > 0.7).

% Rule 7: Transisi Harmonis (Ideal untuk rekomendasi)
% Terjadi jika jarak graf <= 0.4
% FOL: ∀X,Y (jarak(X,Y) ≤ 0.4 → transisi_harmonis(X,Y))
transisi_harmonis(X, Y) :-
    jarak_graf(X, Y, Jarak),
    Jarak =< 0.4.

% Rule 8: Kesimpulan Butuh Bridge
% FOL: ∀X,Y (transisi_kasar(X,Y) → butuh_lagu_bridge(X,Y))
butuh_lagu_bridge(X, Y) :-
    transisi_kasar(X, Y).

% Rule 9: Kesimpulan Rekomendasi Urutan
% FOL: ∀X,Y (transisi_harmonis(X,Y) → rekomendasi_urutan(X,Y))
rekomendasi_urutan(X, Y) :-
    transisi_harmonis(X, Y).

% =================================================================
% END OF FILE
% =================================================================
