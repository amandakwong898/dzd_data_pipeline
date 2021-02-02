# dzd_data_pipeline
a data pipeline and structure for clinical bacterial isolate data

SP1.fastq:
  - genomics data file

parse_and_load.py:
  - FASTQ parsing and database loading
    • Parse the FASTQ file SP1.fastq and extract the DNA sequences
    • Count all the 21-mers within the sequences
    • Using the PySQLite Python API for SQLite:
      o Create a data.db SQLite database
      o Create a kmer table in data.db with two columns,(1)the k-mer string, (2)the count 
      o Fill the table with the 21-mer counts
      
match.py:
  - Matching DNA sequences
  When comparing DNA sequencing, often we are looking for similar but not necessarily identical sequences. Consider Hospital-Acquired Infection (HAI), scenarios in which a patient in a hospital gets infected by another patient, sometimes due to inadequate sanitation. To detect this, we compare DNA samples from patient A and patient B to see how closely related they are. Bacterial DNA mutates frequently, so even in the case of a very recent infection, the two samples may not be identical.
    • returns a set (unique elements) containing all k-mers in seq that match kseq with at most two letters different

    For example, given
    kseq = 'ACGT' seq = 'ACACACGT'
    the k-mers in seq (in order) are 'ACAC', 'CACA', 'ACAC', 'CACG', and 'ACGT'. The result is ['ACAC', 'ACGT']

