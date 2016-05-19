tf-dna-sbatch
=============

Scripts to orchestrate TF-DNA binding predictions

## Steps

1. Generate predictions using `sbatch-script-2016-04-21.sh`, customizing `predict_genome_wrapper.py` as needed
2. Combine per-chromosome predictions into whole-genome, and filter based on threshold


Below is documentation of software and data versions used.

## Software versions:

- [SVR_models 1.1.1](https://github.com/Duke-GCB/SVR_models/releases/tag/1.1.1)
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

- /data/sciencesupport/tf-dna-predictions/models/Ning/TF\_general/SVR/model\_files\_final:

        0fb3b1167caef14dbb2f14dd8d3bba8e  bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACATG_1a2a3mer_format.model
        ec406cc079a00941d905977a50e9e10a  bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACGAG_1a2a3mer_format.model
        74323f39f91b998d838d6afb045a5a5b  bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACGCG_1a2a3mer_format.model
        569fb2cb8cdb922b315f64b231c95347  bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACGTG_1a2a3mer_format.model
        aff3b40f2b0106288437b2ffe4a41b10  bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CATGCG_1a2a3mer_format.model
        0f3fd0207dde818e912bb2bcafc27593  bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACATG_1a2a3mer_format.model
        fb67344a71eb5002a8d48cb7efbde3bb  bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACGAG_1a2a3mer_format.model
        fb84ded0f4f8bc6fc32af68a61722bfa  bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACGCG_1a2a3mer_format.model
        71beb6f70ea673c9324d76a26826ce33  bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACGTG_1a2a3mer_format.model
        a42626bc99f00b1d2579e9d1a0634ccb  bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CATGCG_1a2a3mer_format.model
        d9eedb3eec8e8168b791af1ddb7659a8  E2F/E2F1_250nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGC_1a2a3mer_format.model
        910ebc067a7516e9fc67d08275f315d6  E2F/E2F1_250nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGG_1a2a3mer_format.model
        960209f3c02dadca1c120ecf78b99ca3  E2F/E2F4_500nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGC_1a2a3mer_format.model
        78e9cf8178f1bca24c1e5565adbcc0fa  E2F/E2F4_500nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGG_1a2a3mer_format.model
        adbd639ed01310c3e72b17eac63c7bd5  ETS/ELK1_100nM_Bound_filtered_normalized_transformed_20bp_GGAA_1a2a3mer_format.model
        40abc9a21ab0bba72bdf35a9dc718f47  ETS/ELK1_100nM_Bound_filtered_normalized_transformed_20bp_GGAT_1a2a3mer_format.model
        0505da09e0a2b5704f0e02d43892cba5  ETS/ETS1_100nM_Bound_filtered_normalized_transformed_20bp_GGAA_1a2a3mer_format.model
        d65309294602b06f746b21a40de28a20  ETS/ETS1_100nM_Bound_filtered_normalized_transformed_20bp_GGAT_1a2a3mer_format.model

