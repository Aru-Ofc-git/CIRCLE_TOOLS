o
    ???b?  ?                   @   s?   d dl Z d dlZd dlZd dlZzd dlZW n   e ?d? d dlZY dZdZdZdZ	dZ
dZdZd	Zd
ZdZe ?d? dd? Zdd? Zdd? Zz	e?  e?  W dS  ey`   e??  Y dS w )?    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35mz

 https://bit.ly/3Hz6Ff5?clearc                   C   s,   t ?d? t ?d? t ?d? t ?d? d S )Nz..zlolcat banner.shz.Textzlolcat MyText.txt)?os?chdir?system? r   r   ?follower.py?header"   s   


r   c                 C   s2   | d D ]}t j?|? t j??  t?d? qd S )N?
g???Q???)?sys?stdout?write?flush?time?sleep)?zZwordr   r   r   ?	logoprint)   s
   
?r   c                  C   s  d} 	 t ?d? ttd t ?}|dk?r?d}| d | d }|d	d
?}z	tj||d?}W n   ttd ? t	?
?  Y |?? d d }t ?d? t?  ttd ? t?d? t ?d? t?  ttd t | ? ttd t |?? d d  d ? t?d? d}g }|?? d d }tt|??D ]K}zDttd t |?? d d | d  t d t d |?? d d | d  ? |?? d d | d }	t?d? |?|	? |d }W q?   Y q?	 tttd ??}
|
?? }|dk?r?t ?d? t?  t ?d? tttd  t ??}t?d!? t ?d? t?  ttd" ? t?d? d#t d$ }|d	d
?}tj||d?}t ?d? t?  |D ]J}d%| }d	|d&?}z	tj||d?}W n
   ttd' ? Y t?d(? |?? d) }|d*k?rvttd+ t | ? ?q;ttd, | d- t | ? ?q;q?ttd. ? q)/Nz5https://circle.robi.com.bd/mylife/appapi/appcall.php?Tzlolcat clean2.shz
     Enter Circle ID: ? Z 3c614faafa20eda7cfe001fbf5d0974dz)op=getFollowerInfoList&offset=0&nickname=z
&limit=100Z(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg)?	x-api-key?	x-app-key)?headersz
     Error?dataZfollowerr   z$

     Your Follower Data Loading...?   z
     Your ID: z
     Total Followers: ?totalr	   r   z
 Nickname: Znicknamez
  Number: ?+Zmsisdng?????????   z-
 Are you sure clean your follower list y/n? ?yz     Enter Your API Key: ?   z$

     Your Request In Prossesing...z?https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&message=Hey!+I'm+Cleaning+My+Follower+List+From+ARU's+System.z&retry=falsezKhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=blockUser&nickname=)r   r   z     No internetg      ??ZrdescZOKz&

      You have successfully blocked z

      ? z
     Please Enter Valid ID)r   r   ?input?green?yellow?requests?get?print?redr
   ?exit?jsonr   r   r   ?range?len?cyan?append?str?white?lowerr   ?mark?purpler   )Zm_url?user?keyZfollowerGetZ
getHeadersZrequ_for_followerr   ?x?idZnickZsure?sZapiZurl1Zheaders1?st?mZurlr   ZrequZrespZenterr   r   r   ?main0   s?   






$
P







?



 ?+?r7   )r   r
   r&   r   r!   r   ZblueZ	lightbluer$   r,   r    r   r)   ?endr/   r.   r   r   r7   ?KeyboardInterruptr%   r   r   r   r   ?<module>   s4    


`?