dna_rna = { 'G':'C', 'C':'G', 'T':'A', 'A':'U'}  # dictionary of dna to rna transcriptions
def to_rna(dna_strand):
    return ''.join([dna_rna[c] for c in dna_strand]) 
    
