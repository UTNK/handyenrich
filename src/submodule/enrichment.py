import numpy     as     np
from   scipy     import stats
from   statsmodels.stats.multitest import multipletests

def enrichment_test(
        class2termlist         ,
        query_termlist         ,
        all_termlist           ,
        alternative = "greater",
        correction  = "fdr_bh"   
        ):

    classlist = list(class2termlist.keys())
    classlist.sort()

    query_termset = set(query_termlist)

    # prep
    
    results = []
    for cl in classlist:

        termset_in_class = set(class2termlist[cl])

        # prep
        in_query_in_class       = []
        in_query_outof_class    = []
        outof_query_in_class    = []
        outof_query_outof_class = []
        
        # classification of KOs
        for term in all_termlist:
            if    ((term     in query_termset) and (term     in termset_in_class)): in_query_in_class      .append(term)
            elif  ((term     in query_termset) and (term not in termset_in_class)): in_query_outof_class   .append(term)
            elif  ((term not in query_termset) and (term     in termset_in_class)): outof_query_in_class   .append(term)
            elif  ((term not in query_termset) and (term not in termset_in_class)): outof_query_outof_class.append(term)
        
        # test
        
        data = np.array([[len(in_query_in_class)   , len(outof_query_in_class   )],
                         [len(in_query_outof_class), len(outof_query_outof_class)]])
        _, p = stats.fisher_exact(data, alternative='alternative'); test="fisher"
        
        # store result
        
        results.append(
            {
            "classname" : cl,
            "stats"     : str(data[0,0])+";"+str(data[0,1])+";"+\
                          str(data[1,0])+";"+str(data[1,1]),
            "p_value"   : p, 
            }
        )
        
    # calculate q values
    
    pvalues = [ r["p_value"] for r in results ]
    qvalues = multipletests(pvalues, method = correction)[1]
    for j, q in enumerate(qvalues):
        results[j]["q_value"] = q
    
    results.sort(key=lambda x: x['p_value'])
    
    return results