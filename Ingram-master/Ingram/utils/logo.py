import os, random

ingram_icon = r"""
          _    __..-:┑
   ║`====╩=╩=======╣ |
==#║_______███_/ @ ║ |
   ╚===.===╦==╦=╤==╩#█
       \___║::║/      
           ║::║|      
           ║::║|      
           ║::║_\     
            ██        
            ██        
            ██        
            ██        
            ██        
"""

ingram_fonts = [
r"""
::::::::::: ::::    :::  ::::::::  :::::::::      :::     ::::    ::::  
    :+:     :+:+:   :+: :+:    :+: :+:    :+:   :+: :+:   +:+:+: :+:+:+ 
    +:+     :+:+:+  +:+ +:+        +:+    +:+  +:+   +:+  +:+ +:+:+ +:+ 
    +#+     +#+ +:+ +#+ :#:        +#++:++#:  +#++:++#++: +#+  +:+  +#+ 
    +#+     +#+  +#+#+# +#+   +#+# +#+    +#+ +#+     +#+ +#+       +#+ 
    #+#     #+#   #+#+# #+#    #+# #+#    #+# #+#     #+# #+#       #+# 
########### ###    ####  ########  ###    ### ###     ### ###       ### 
"""
]

def _generate():
    i_lines = [l for l in ingram_icon.split('\n') if l.strip()]
    f_lines = random.choice(ingram_fonts).strip('\n').split('\n')
    iw, fw = max(len(l) for l in i_lines), max(len(l) for l in f_lines)
    h = max(len(i_lines), len(f_lines))
    while len(i_lines) < h: i_lines.append(' ' * iw)
    while len(f_lines) < h: f_lines.append(' ' * fw)
    return [i_lines, f_lines]

logo = _generate()