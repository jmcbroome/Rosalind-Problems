
# coding: utf-8

# In[3]:


from sequenceAnalysis import *


# In[13]:


genome = FastAreader('testGenome.fa')


# In[ ]:


for head, seq in genome.readFasta():
    current_genome = NucParams(seq)
    seq_length = (current_genome.nucCount()/1000000)
    gc = 100*((seq.count('G')+seq.count("C"))/current_genome.nucCount())
    codon_usage = []
    rel_freq_dict = current_genome.codonComposition()
    #going to make a series of strings for printing in the next step 
    for key, value in NucParams.rnaCodonTable.items():
        freq = rel_freq_dict.get(key)
        count = current_genome.codon.count(key)
        codon_usage.append('{0} : {1} {2} ({3}) \n'.format(key, value, freq, count))
    codon_usage_string = ''.join(codon_usage)
    print(('File Head: {0} \n \n sequence length = {1} Mb \n \n GC content = {2} \n \n {3}').format(head, seq_length, gc, codon_usage_string))

