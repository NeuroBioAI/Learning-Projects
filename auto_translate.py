
def auto_translate(gseq: str)->str:
    if 't' in gseq:
        nuaa={'ttt':'F','ttc':'F',
              'tta':'L','ttg':'L','ctt':'L','ctc':'L','cta':'L','ctg':'L',
              'att':'I','atc':'I','ata':'I',
              'atg':'M',
              'gtt':'V','gtc':'V','gta':'V','gtg':'V',
              'tct':'S','tcc':'S','tca':'S','tcg':'S','agt':'S','agc':'S',
              'cct':'P','ccc':'P','cca':'P','ccg':'P',
              'act':'T','acc':'T','aca':'T','acg':'T',
              'gct':'A','gcc':'A','gca':'A','gcg':'A',
              'tat':'Y','tac':'Y',
              'cat':'H','cac':'H',
              'caa':'Q','cag':'Q',
              'aat':'N','aac':'N',
              'aaa':'K','aag':'k',
              'gat':'D','gac':'D',
              'gaa':'E','gag':'E',
              'tgt':'C','tgc':'C',
              'tgg':'W',
              'cgt':'R','cgc':'R','cga':'R','cgg':'R','aga':'R','agg':'R',
              'ggt':'G','ggc':'G','gga':'G','ggg':'G'}
    
        stop=['taa','tag','tga']
        pseq=[] 
        for i in range(0,len(gseq),3):
            gseq1=gseq[i:i+3]
            if len(gseq1)<=3:
                if gseq1 in stop:
                    break
            if gseq1 in nuaa.keys():
                pseq.append(nuaa[gseq1])

            protein=''.join(pseq)    
     
    else:
        nuaa={'uuu':'F','uuc':'F',
              'uua':'L','uug':'L','cuu':'L','cuc':'L','cua':'L','cug':'L',
              'auu':'I','auc':'I','aua':'I',
              'aug':'M',
              'guu':'V','guc':'V','gua':'V','gug':'V',
              'ucu':'S','ucc':'S','uca':'S','ucg':'S','agu':'S','agc':'S',
              'ccu':'P','ccc':'P','cca':'P','ccg':'P',
              'acu':'T','acc':'T','aca':'T','acg':'T',
              'gcu':'A','gcc':'A','gca':'A','gcg':'A',
              'uau':'Y','uac':'Y',
              'cau':'H','cac':'H',
              'caa':'Q','cag':'Q',
              'aau':'N','aac':'N',
              'aaa':'K','aag':'k',
              'gau':'D','gac':'D',
              'gaa':'E','gag':'E',
              'ugu':'C','ugc':'C',
              'ugg':'W',
              'cgu':'R','cgc':'R','cga':'R','cgg':'R','aga':'R','agg':'R',
              'ggu':'G','ggc':'G','gga':'G','ggg':'G'}
    
        stop=['uaa','uag','uga']
        pseq=[] 
        for i in range(0,len(gseq),3):
            gseq1=gseq[i:i+3]
            if len(gseq1)<=3:
                if gseq1 in stop:
                    break
            if gseq1 in nuaa.keys():
                pseq.append(nuaa[gseq1])
    
        protein=''.join(pseq) 
    return protein