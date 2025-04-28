from __future__ import unicode_literals
import pandas as pd
from templates import *
from pyarabic.araby import strip_tashkeel
from IPython.display import display, HTML
#q=pd.read_csv('m.csv',sep='\t',encoding='utf-16')
q=pd.read_csv('corpus/Quranic.csv',sep='\t',encoding='utf-16')
pos=pd.read_csv('corpus/pos.csv',sep='\t',encoding='utf-16')
pos_ar={pos.pos.iloc[i]:pos.pos_ar.iloc[i] for i in range(len(pos))}
pos_en={pos_ar[i]:i for i in pos_ar}
ctags={pos.pos.iloc[i]:pos.color.iloc[i] for i in range(len(pos))}
##################
rel=pd.read_csv('corpus/RelLabels.csv',sep='\t',encoding='utf-16')
csyns={rel.rel_en.iloc[i]:rel.rel_color.iloc[i] for i in range(len(rel))}

########
rel={rel.rel_ar.iloc[i]:rel.rel_nho.iloc[i] for i in range(len(rel))}
#######################
segment={'PREFIX': 'بادئة',
         'STEM'  : 'أصل',
         'SUFFIX': 'لاحقة'}
verb_form={'(I)'   : 'فَعَلَ',
           '(II)'  : 'فَعَّلَ',
           '(III)' : 'فَاعَلَ',
           '(IV)'  : 'أَفْعَلَ',
           '(IX)'  : 'إِفْعَلَّ',
           '(V)'   : 'تَفَعَّلَ',
           '(VI)'  : 'تَفَاعَلَ',
           '(VII)' : 'إِنْفَعَلَ',
           '(VIII)': 'إِفْتَعَلَ',
           '(IX)'  : 'إِفْعَلَّ',
           '(X)'   : 'إِسْتَفْعَلَ',
           '(XI)'  : 'فَعْلَلَ',
           '(XII)' : 'تَفَعْلَلَ',
           '_' : '_'}
verb_aspect = {'PERF': 'فعل ماضي',
             'IMPF': 'فعل مضارع',
             'IMPV': 'فعل أمر',
             '_' : '_'}
nominal_state={'DEF'  : 'معرفة',
              'INDEF': 'نكرة',
              '_' : '_'}
verb_mood = {'MOOD:IND': 'مرفوع',
             'MOOD:JUS': 'مجزوم',
             'MOOD:SUBJ': 'منصوب',
             '_' : '_'}
special_group={'SP:<in~': 'من اخوات ان',
               'SP:kaAd': 'من اخوات كاد',
               'SP:kaAn': 'من اخوات ان',
               '_' : '_'}
nominal_case={'NOM': 'مرفوع',
              'ACC': 'منصوب',
              'GEN': 'مجرور',
              '_' : '_'}
derived_nouns={'ACT_PCPL':'اسم فاعل',
              'PASS_PCPL':'اسم مفعول',
              'VN':'مصدر',
              '_':'_'}
verb_voice={'ACT': 'مبني للمعلوم',
            'PASS': 'مبني للمجهول',
            '_':'_'}
person={'1': 'واحد',
        '2': 'اثنين',
        '3': 'ثلاثة',
        '_':'_'}
gender={'M': 'مذكر',
        'F': 'مؤنث',
        '_':'_'}
number={'S': 'مفرد',
        'D': 'مثنى',
        'P': 'جمع',
        '_':'_'}
prefixs ={'A:EQ+': 'همزة تسوية',
         'A:INTG+': 'همزة استفهام',
         'Al+': 'ال التعريف',
         'bi+': 'باء الجر',
         'f:CAUS+': 'فاء السببية',
         'f:CONJ+': 'فاء العطف',
         'f:REM+': 'فاء الإستئناف',
         'f:RSLT+': 'فاء الشرط',
         'f:SUP+': 'فاء الزائدة',
         'ha+': 'هاء النداء',
         'ka+': 'كاف الجر',
         'l:EMPH+': 'لام التوكيد',
         'l:IMPV+': 'لام الأمر',
         'l:P+': 'لام الجر',
         'l:PRP+': 'لام التعليل',
         'sa+': 'سين المستقبل',
         'ta+': 'تاء النداء',
         'w:CIRC+': 'واو الظرفية',
         'w:COM+': 'واو المعية',
         'w:CONJ+': 'واو العطف',
         'w:P+': 'واو الجر',
         'w:REM+': 'واو الإستئناف',
         'w:SUP+': 'واو الزائدة',
         'ya+': 'ياء النداء',
         '_': '_'}
suffixs={'VOC:m' : 'ميم النداء',
        'EMPH:n': 'نون التوكيد',
        'PRON': 'ضمير متصل',
        'l:P+': 'لام الجر',
        '_': '_'}

#######################
def get_morph_ver(ayah_id):
    v=q[(q.sentence_id==ayah_id)&(q.location!='_')]
    wt=get_words_ids(v)
    u=list(v.uthmani_token)
    p=list(v.pos)
    #########
    w=[[{'text':u[i[j]]+'&zwj;','tcolor':ctags[p[i[j]]]} if j!=len(i)-1 else {'text':u[i[j]],'tcolor':ctags[p[i[j]]]}  for j in range(len(i))] for i in wt]
    ##w=[[{'text':u[j],'tcolor':ctags[p[j]]} for j in i] for i in wt]
    m=v[['uthmani_token', 'pos', 'prefix', 'suffix', 'verb_aspect', 'derived_nouns', 'nominal_state', 'special_group', 
     'verb_voice', 'number', 'gender', 'verb_mood', 'nominal_case', 'lemma_ar', 'verb_form', 'root_ar']].copy()
    ############
    m['prefix']=[prefixs[i] for i in m.prefix]
    m['suffix']=[suffixs[i] for i in m.suffix]
    m['derived_nouns']=[derived_nouns[i] for i in m.derived_nouns]
    m['verb_aspect']=[verb_aspect[i] for i in m.verb_aspect]
    m['nominal_state']=[nominal_state[i] for i in m.nominal_state]
    m['special_group']=[special_group[i] for i in m.special_group]
    m['verb_voice']=[verb_voice[i] for i in m.verb_voice]
    m['number']=[number[i] for i in m.number]
    m['gender']=[gender[i] for i in m.gender]
    m['verb_mood']=[verb_mood[i] for i in m.verb_mood]
    m['nominal_case']=[nominal_case[i] for i in m.nominal_case]
    m['verb_form']=[verb_form[i] for i in m.verb_form]
    ###############
    m=[[remove_noise(m.iloc[j].to_dict()) for j in i] for i in wt]
    parer=[{'words':w[i], 'morph':m[i]} for i in range(len(w))]
    return parer
#######################
def get_words_ids(v):
    wt=[]
    w=list(v.word_id)
    m=[0]
    for i in range(1,len(v)):
        if (w[i]==w[i-1]):
            m.append(i)                
        else:
            wt.append(m)
            m=[]
            m.append(i)                
    wt.append(m)
    return wt


def remove_noise(j):
    d=[]
    for i in j:
        if j[i] =='_':
            d.append(i)
    for i in d:
        del j[i]
    k=[{'ptext':'', 'text':j['uthmani_token'],'stext':': ','tcolor':ctags[j['pos']],'tfont':'hafs'},
       {'ptext':'', 'text':pos_ar[j['pos']],'stext':'','tcolor':ctags[j['pos']],'tfont':'Traditional Arabic'}]
    if len(j)>2:
        j=dict(list(j.items())[2:])
        for i in j:
            k1=[get_morph_det(i,j[i]) for i in j]
        k.extend(k1)
    return k

def get_morph_det(a1,a2):
    d1={'ptext':' «','text':a2,'stext':'»','tcolor':'black','tfont':'Traditional Arabic'}
    d2={'ptext':' ','text':a2,'stext':'','tcolor':'black','tfont':'Traditional Arabic'}
    if a1=='prefix':
        d=d1
    elif a1=='suffix':
        d=d1
    elif a1=='derived_nouns':
        d=d1
    elif a1=='verb_aspect':
        d=d1
    elif a1=='nominal_state':
        d=d2
    elif a1=='number':
        d={'ptext':' لل&zwj;','text':a2,'stext':'','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='gender':
        d={'ptext':' ال&zwj;','text':a2,'stext':'','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='nominal_case':
        d={'ptext':' ','text':a2,'stext':'','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='verb_mood':
        d={'ptext':' ','text':a2,'stext':'','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='special_group':
        d={'ptext':' ','text':a2,'stext':'','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='verb_voice':
        d={'ptext':' ','text':a2,'stext':'','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='lemma_ar':
        d={'ptext':'، اللما له «','text':a2,'stext':'»','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='root_ar':
        d={'ptext':'، الجذر له «','text':a2,'stext':'»','tcolor':'black','tfont':'Traditional Arabic'}
    elif a1=='verb_form':
        d={'ptext':'، النمط له «','text':a2,'stext':'»','tcolor':'black','tfont':'Traditional Arabic'}
    return d

##############
def get_syntax(sid):
    syntax1=[];syntax2=[];dep=[];cons=[];tids=[]
    m1=q[q.sentence_id==sid]
    token_id=list(m1[(m1.sentence_id==sid)&(m1.location!='_')].token_id)
    loc=[[d,m1.loc1.iloc[d]] for d in range(len(m1)) if m1.loc1.iloc[d]!='_']
    l1=[i[0] for i in loc]
    l2=[int(i[1]) for i in loc]
    for j in range(len(m1)):
        if m1.location.iloc[j]!='_':
            pars=[]
            if (m1.rel_label_ar.iloc[j] not in ['root','NonRel']) and (m1.constituents.iloc[j]=='_'):
                rp=m1.rpos.iloc[j].split(' ')
                if len(rp) == 2:
                    rp= rp[0]+' ال&zwj;'+rp[1]
                else:
                    rp=rp[0]
                uth=m1.re_uthmani.iloc[j]
                pars.append({'ptext':'. وهو ','text':rel[m1.rel_label_ar.iloc[j]]+'&zwj;',
                             'stext':'','tcolor':csyns[m1.rel_label.iloc[j]],'tfont':'Traditional Arabic'})
                pars.append({'ptext':'&zwj;','text':rp,'stext':'','tcolor':ctags[pos_en[m1.rpos.iloc[j]]],'tfont':'Traditional Arabic'})
                if uth[0]=='(':
                    elips='المحذوف'
                    if m1.rpos.iloc[j][-1]=='ة':
                        elips='المحذوفة'
                    pars.append({'ptext':' ','text':elips,'stext':'.','tcolor':'black','tfont':'Traditional Arabic'})
                else:
                    pars.append({'ptext':' ﴿','text':uth,'stext':'﴾','tcolor':'green','tfont':'Traditional Arabic'})
                ###########
                case=get_case(m1.nominal_case.iloc[j],m1.verb_mood.iloc[j],m1.uthmani_token.iloc[j],m1.uthmani_token.iloc[j-1],m1.rpos.iloc[j])
                if case!='':
                     pars.append(case)
            #############
            elif m1.rel_label_ar.iloc[j] =='root':
                pred=list(m1[(m1.rel_label_ar=='خبر')&(m1.ref_token_id==j)].token_id)
                if len(pred)>0:
                    mobtda='. وهو مبتداء للجملة الاسمية.'
                    if m1.location.iloc[pred[0]]=='_':
                        mobtda='. وهو مبتداء للجملة الاسمية وخبره محذوف.'        
                    pars.append({'ptext':'','text':mobtda,'stext':'','tcolor':'black','tfont':'Traditional Arabic'})
            #############
            else:
                pars.append({'ptext':'','text':'','stext':'','tcolor':'black','tfont':'Traditional Arabic'})
                
            dep.append(pars)
        if j in l2:
            d=[l1[i] for i in range(len(l2)) if l2[i]==j]
            for c in d[::-1]:
                con=[]
                rp=m1.rpos.iloc[c].split(' ')
                if len(rp) == 2:
                    rp= rp[0]+' ال&zwj;'+rp[1]
                else:
                    rp=rp[0]
                tid=token_id.index(j)
                con.append({'ptext':'','text':m1.constituent_label.iloc[c],'stext':'',
                            'tcolor':ctags[m1.constituent_label_en.iloc[c]],'tfont':'Traditional Arabic'})
                con.append({'ptext':' ﴿','text':m1.constituents.iloc[c],'stext':'﴾.',
                            'tcolor':'green','tfont':'Traditional Arabic'})
                r=rel[m1.rel_label_ar.iloc[c]]+'&zwj;'
                if m1.rel_label_ar.iloc[c]=='root':
                    r= 'مرتبطة بجملة اخرى.'
                con.append({'ptext':' ','text':r,'stext':'', 'tcolor':csyns[m1.rel_label.iloc[c]],'tfont':'Traditional Arabic'})
                if m1.re_uthmani.iloc[c][0]=='(':
                    if rp[-1]=='ة':
                        rp=rp+' المحذوفة'
                    else:
                        rp=rp+' المحذوف'
                con.append({'ptext':'','text':rp,'stext':'',
                            'tcolor':ctags[pos_en[m1.rpos.iloc[c]]],'tfont':'Traditional Arabic'})
                con.append({'ptext':' ﴿','text':m1.re_uthmani.iloc[c],'stext':'﴾.',
                            'tcolor':'green','tfont':'Traditional Arabic'})
                cons.append(con)
                tids.append(tid)
    #
    d=get_words_ids(q[(q.sentence_id==sid)&(q.location!='_')])
    parse_dep=[[dep[j] for j in i] for i in d]
    ####
    parse_cons=[[cons[tids.index(j)] for j in i if j in tids] for i in d]
    return parse_dep,parse_cons

def get_case(nominal_case,verb_mood,uthmani_token,uthmani_token1,rpos):
    p=''
    if verb_mood=='مجزوم':
        if uthmani_token[-1]=='ْ':
            p={'ptext':' ','text':verb_mood,'stext':' بالسكون لانه معتل الاخر.','tcolor':'DarkOrchid','tfont':'Traditional Arabic'}
    elif verb_mood=='منصوب':
        if uthmani_token[-1]=='َ':
            p={'ptext':' ','text':verb_mood,'stext':' وعلامة نصبه الفتحة الظاهرة على اخره.','tcolor':'GreenYellow','tfont':'Traditional Arabic'}
    else:
        p={'ptext':'','text':'.','stext':'','tcolor':'black','tfont':'Traditional Arabic'}            
    if nominal_case=='مرفوع':
        if uthmani_token[-1]=='ُ':
            p={'ptext':' ','text':nominal_case,'stext':' وعلامة رفعه الضمة الظاهرة على اخره.','tcolor':'OrangeRed','tfont':'Traditional Arabic'}
    elif nominal_case=='منصوب':
        if uthmani_token[-1]=='َ':
            p={'ptext':' ','text':nominal_case,'stext':' وعلامة نصبه الفتحة الظاهرة على اخره.','tcolor':'GreenYellow','tfont':'Traditional Arabic'}
    elif nominal_case=='مجرور':
        if uthmani_token[-1]=='ِ':
            if rpos=='حرف جر':
                nominal_case=''
            p={'ptext':' ','text':nominal_case,'stext':' وعلامة جره الكسره الظاهرة على اخره.','tcolor':'red','tfont':'Traditional Arabic'}                
    else:
        p={'ptext':'','text':'.','stext':'','tcolor':'black','tfont':'Traditional Arabic'}            
    return p
#############
def get_iirab_structure(sid):
    morph=get_morph_ver(sid)
    parse_dep,parse_cons=get_syntax(sid)
    ws=[[j for j in i['words']] for i in morph]
    ms=[[[d for d in j] for j in i['morph']] for i in morph]
    ss=[[[d for d in j] for j in i] for i in parse_dep]
    ss=[[ms[i][j]+ss[i][j] for j in range(len(ms[i]))] for i in range(len(ms))]
    cs=[[[d for d in j] if len(i) else '' for j in i] for i in parse_cons]
    for i in range(len(cs)):
        if len(cs[i])!=0:
            ss[i]=ss[i]+cs[i]
    return ws,ss
###################################
TABLE="""    <div class="table-container">
        <table dir="rtl">
            <tbody>
              {table}
            </tbody>
          </table>
    </div>"""
TR="""          <tr>
                {nho}
              </tr>"""
TD1="""         <td dir="rtl" class="td1-cell-style">
                    {para}
                </td>"""
TD2="""         <td dir="rtl" class="td2-cell-style">
                    {para}
                </td>"""
PARA="""                  <p dir="RTL" class="paragraph-style">
                    {spans}
                  </p>"""
SPAN="""                <span class="word-style-class" style="color: {};">{}</span>"""
#&zwj;
def get_iirab_table(sid):
    w,s=get_iirab_structure(sid)
    word=['\n'.join([SPAN.format(*(j['tcolor'],j['text'])) for j in i]) for i in w]
    word=[TD1.format(para=PARA.format(spans=i)) for i in word]
    iirab=[[sum([[SPAN.format(*('black',j['ptext'])),SPAN.format(*(j['tcolor'],j['text'])),SPAN.format(*('black',j['stext']))] 
             for j in d],[]) for d in i] for i in s]
    iirab=[['\n'.join([d for d in j if d.find('></span>')==-1]) for j in i] for i in iirab]
    iirab=[TD2.format(para='\n'.join([PARA.format(spans=j) for j in i])) for i in iirab]
    table=TABLE.format(table='\n'.join([TR.format(nho='\n'.join([word[i],iirab[i]])) for i in range(len(word))]))
    return table
