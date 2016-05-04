tf-dna-sbatch
=============

Scripts to orchestrate TF-DNA binding predictions

## Steps

1. Generate predictions using `sbatch-script-2016-04-21.sh`, customizing `predict_genome_wrapper.py` as needed
2. Combine per-chromosome predictions into whole-genome, and filter based on threshold


Below is documentation of software and data versions used.

## Software versions:

- [SVR_models 1.1.0](https://github.com/Duke-GCB/SVR_models/releases/tag/1.1.0)
- [LIBSVM 3.21](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) [github](https://github.com/cjlin1/libsvm/releases/tag/v321)

SVR_Models repo includes a Dockerfile for Python 2.7.11 that installs libsvm too

## Data File checksums:

### Genomes

- /data/sciencesupport/tf-dna-predictions/genomes

        530d89d3ef07fdb2a9b3c701fb4ca486  hg19.fa
        b2aee9f885accc00531e59c4736bee63  hg38.fa

hg38 from http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz and gunzipped
hg19 from http://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit and converted to fa with [twoBitToFa](http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa)

### Models

- /data/sciencesupport/tf-dna-predictions/models:

        e7a85675d7d025d65529c00f1468a534  E2F1-bestSVR.model
        583cc424e209f9d8eef38ef396bcbed7  E2F4-bestSVR.model

- /data/sciencesupport/tf-dna-predictions/models/Ning/TF_general/SVR:

        dde303bd999160e7c144f1d733aeb9be  E2F1_250nM_Bound_filtered_normalized_34bp_GCGC_1a2a3mer_format.model
        5279cf828d91ec341407a47439a2f1f3  E2F1_250nM_Bound_filtered_normalized_34bp_GCGG_1a2a3mer_format.model
        7d311b8f1a5640d9d4bfb35fe7bb502c  E2F4_500nM_Bound_filtered_normalized_34bp_GCGC_1a2a3mer_format.model
        604d2751ea8aa5005267495ffd83ed22  E2F4_500nM_Bound_filtered_normalized_34bp_GCGG_1a2a3mer_format.model
        61cef674ba4a1d3118f23fcc761c6bdc  ELK1_100nM_Bound_filtered_normalized_GGAA_1a2a3mer_format.model
        0c43ba23c50d5dd4adfd2f31cd48d76e  ELK1_100nM_Bound_filtered_normalized_GGAT_1a2a3mer_format.model
        7e44110f0af2795fcf873b893ef4f5de  ETS1_100nM_Bound_filtered_normalized_GGAA_1a2a3mer_format.model
        b72cc895cb029a92cb64f81817630ce0  ETS1_100nM_Bound_filtered_normalized_GGAT_1a2a3mer_format.model
        5065ab68bc797c739c03937fd6dc2a18  HisMadMax_Bound_filtered_normalized_CACATG_1a2a3mer_format.model
        9e6781737c571fd63c38652703c6b946  HisMadMax_Bound_filtered_normalized_CACGAG_1a2a3mer_format.model
        b9622ed777116eaa7576f24fe823818b  HisMadMax_Bound_filtered_normalized_CACGCG_1a2a3mer_format.model
        09870d48a598e4baf925682c261990fe  HisMadMax_Bound_filtered_normalized_CACGTG_1a2a3mer_format.model
        8aeb792f2e372757e1b574f4445b3bcd  HisMadMax_Bound_filtered_normalized_CATGCG_1a2a3mer_format.model
        b98904979b198715885f219acc49cdf4  HisMycMax_Bound_filtered_normalized_CACATG_1a2a3mer_format.model
        0732afafe91e5e4bc024f3ae81225e7b  HisMycMax_Bound_filtered_normalized_CACGAG_1a2a3mer_format.model
        af05caa20f11bb99518990a68f15bec7  HisMycMax_Bound_filtered_normalized_CACGCG_1a2a3mer_format.model
        cd0bd0dc0126906890073fc99c83b122  HisMycMax_Bound_filtered_normalized_CACGTG_1a2a3mer_format.model
        528829885dc92c630e736d13aad9f42e  HisMycMax_Bound_filtered_normalized_CATGCG_1a2a3mer_format.model
