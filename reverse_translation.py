###Codon optimize in Host of Yeast (reverse translation):
##useing from dictionary:
aanu={}
aanu['F']={0.58:'ttt',0.42:'ttc'}
aanu['L']={0.14:'tta',0.13:'ttg',0.12:'ctt',0.10:'ctc',0.04:'cta',0.47:'ctg'}      
aanu['I']={0.49:'att',0.39:'atc',0.11:'ata'}
aanu['M']={1.00:'atg'}
aanu['V']={0.28:'gtt',0.20:'gtc',0.17:'gta',0.35:'gtg'}
aanu['S']={0.17:'tct',0.15:'tcc',0.14:'tca',0.16:'agt',0.25:'agc'}
aanu['P']={0.18:'cct',0.13:'ccc',0.20:'cca',0.49:'ccg'}
aanu['T']={0.19:'act',0.40:'acc',0.17:'aca',0.25:'acg'}
aanu['A']={0.18:'gct',0.26:'gcc',0.23:'gca',0.33:'gcg'}
aanu['Y']={0.59:'tat',0.41:'tac'}
aanu['H']={0.57:'cat',0.43:'cac'}
aanu['Q']={0.34:'caa',0.66:'cag'}
aanu['N']={0.49:'aat',0.51:'aac'}
aanu['K']={0.74:'aaa',0.26:'aag'}
aanu['D']={0.63:'gat',0.37:'gac'}
aanu['E']={0.68:'gaa',0.32:'gag'}
aanu['C']={0.46:'tgt',0.54:'tgc'}
aanu['W']={1.00:'tgg'}
aanu['R']={0.36:'cgt',0.11:'cgg',0.07:'aga',0.04:'agg'}
aanu['G']={0.35:'ggt',0.37:'ggc',0.13:'gga',0.15:'ggg'}

pseq='MTEYKLVVVGAGGVGkSALTIQLIQNHFVDEYDPTIEDSYRkQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVkDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAkTRQRVEDAFYTLVREIRQYRLKKISKEEkTPGCVKIKKCIIM'
  
gseq=[]       
for aa in pseq:
    if aa in aanu.keys():
        maxkey=max(aanu[aa].keys())##Optimizeing
        gseq.append(aanu[aa].get(maxkey)) 
dnaseq=''.join(gseq)       
print(dnaseq)        
        
    
    
    
    
    


