These are the methods behind the data shown in the two browsers. The text follows the Methods and Supplementary Methods of the manuscript (reference to be added on publication), which also describe the further analyses listed at the end of this page.

## Experiments

### Mice and diets

- **Approval:** studies were conducted in compliance with Danish regulations, under an experimental animal license approved by the Animal Experiments Inspectorate, Ministry of Food, Agriculture, and Fisheries, Danish Veterinary and Food Administration (Dyreforsøgstilsynet, 2024-15-0201-01672).
- **Total kidney:** two male C57Bl/6JBomTac mice (Taconic Biosciences), 10 weeks old. The cells of the two mice were pooled before sorting.
- **DCT cells:** transgenic mice expressing enhanced green fluorescent protein (eGFP) throughout the distal convoluted tubule (DCT) under the control of the parvalbumin (PvAlb) promoter (B6;129P2-Pvalb<sup>tm1(cre)Arbr</sup>/J; kindly provided by Dr. H. Monyer, University of Heidelberg, Germany).
  - The mice had been backcrossed for more than 10 generations to C57Bl/6JBomTac mice.
  - The genotype was verified by PCR on genomic DNA from tail biopsies (primers 5’-TAACTATGCGGCATCAGAGC-3’ and 5’-GCCTCCAGGTCGACTCTAGAG-3’).
- **Diets:** the PvAlb-GFP mice received a control diet or a zero-potassium (zero-K) diet for 4 days.
- **Pools:** the cells of the 3 mice of each diet condition were pooled, giving one pool per condition. Condition and pool therefore cannot be separated, and cells are not animal-level replicates.
- **Sort plates:** each pool was sorted onto two 384-well plates (P1, P2), which are technical sort plates of the pooled cells. Control and zero-K cells were sorted and acquired in the same sessions.
- **Housing:** standard cages, a 12:12 h artificial light-dark cycle, 21 ± 2 °C and 55% ± 2% humidity, with free access to water and standard rodent diet (1324 pellets, Altromin) until use.

### Kidney single-cell suspension

- Mice were anesthetized with isoflurane and perfused through the left ventricle of the heart with 10 mL of collagenase solution: 2 mg/mL collagenase B (Roche), 250 μg/mL collagenase IV (Gibco), 125 mM NaCl, 0.4 mM KH<sub>2</sub>PO<sub>4</sub>, 1.6 mM K<sub>2</sub>HPO<sub>4</sub>, 1 mM MgSO<sub>4</sub>, 10 mM Na-acetate, 1 mM α-ketoglutarate, 1.3 mM Ca-gluconate, 5 mM glycine, 30 mM glucose and 5 μg/mL DNase I (Sigma), pH 7.4.
- Mice were euthanized by cervical dislocation. The kidneys were rapidly excised and cut into pieces of about 1 mm³, and single-cell suspensions were prepared as described previously (Kortenoeven et al., *Am J Physiol Renal Physiol* 2021;320:F908–F921):
  1. The pieces were incubated at 37 °C in collagenase solution with continuous mixing at 850 rpm. After 10 min, half of the solution was replaced with fresh solution, and the incubation continued for 10 min.
  2. The samples were centrifuged for 3 min at 200 g and the supernatant was removed.
  3. Cells were washed with a trypsin/EDTA solution (Lonza) containing 10 mM HEPES, 30 mM glucose and 50 µg/mL DNase I, resuspended in trypsin/EDTA solution and incubated for 15 min at 37 °C with regular mixing.
  4. Cells were washed in DMEM/Ham F12 medium (Gibco) containing 5% FBS, 30 mM glucose, 10 mM HEPES and DNase I, rinsed, and stored in PBS.
- The suspensions were sorted immediately at the FACS Core Facility, Aarhus University, Denmark.

### Cell sorting and in-well sample preparation

- **Filtering:** suspensions were passed through a 50 µm filter (BD Biosciences) to remove cell clumps.
- **Drop-position test:** before each sort, a small fraction of the suspension was resuspended in horseradish peroxidase (100 µg/mL, ChemCruz), and single cells were sorted into a 384-well plate holding 2 µL of 3,3’,5,5’-tetramethylbenzidine high-sensitivity substrate (BioLegend). A color change to blue verified that single drops reached the wells.
- **Sorter:** 6-laser Bigfoot cell sorter with SQS Software v.1.9.4 (Thermo Fisher), 100 µm nozzle, 20 psi, single-cell sort mask and straight-down sorting, with all events of no interest deflected.
- **Gating:** dead cells were excluded by propidium iodide staining (8 µg/mL, Invitrogen).
  - Total kidney cells were gated as non-debris, singlets and live cells.
  - For cells of PvAlb-GFP mice, a gate on GFP fluorescence was added.
- **Plates:** cells were sorted directly into the wells of a LoBind 384-well plate (Eppendorf) holding 2 µL of 20 mM triethylammonium bicarbonate (TEAB) buffer.
- **Lysis and digestion in the wells:**
  1. Plates were centrifuged at 1,000 g for 1 min, snap frozen on dry ice for 10 min and incubated for 5 min at 95 °C.
  2. A non-contact nanoliter dispenser (iDOT, Cytena) added 200 nL of Lys-C (10 ng/µL, Thermo Fisher) to each well, and the covered plate was incubated at 37 °C for 2 h.
  3. Then 200 nL of trypsin (10 ng/µL, Thermo Fisher) was added, and the covered plate was incubated at 37 °C overnight.
  4. Finally, 100 nL of 10% trifluoroacetic acid was added, and the covered plate was stored at −80 °C until LC-MS analysis.

### LC-MS

- **Instruments:** Vanquish Neo HPLC coupled to an Orbitrap Ascend mass spectrometer with a FAIMS Pro Duo interface (Thermo Fisher); a 50 cm low-load µPAC Neo column (Thermo Fisher) in a one-column setup. Solution B was 80% acetonitrile with 0.1% formic acid. Data were acquired in data-independent acquisition (DIA) mode.

| | Total kidney cells | DCT cells |
| --- | --- | --- |
| Gradient time | 30 min | 25 min |
| Loading | flow ramping to 500 nL/min for 4 min | flow ramping to 500 nL/min for 2.1 min |
| Separation at 200 nL/min | 16 min of 5–22% B, then 5 min of 22–40% B | 10.5 min of 5–22.5% B, then 7.5 min of 22.5–40% B |
| Column rinse at 500 nL/min | 5 min of 99% B | 4.9 min of 99% B |
| FAIMS compensation voltage | −45 V | −50 V |
| MS1 scan range (m/z) | 375–1010 | 400–800 |
| MS1 | Orbitrap resolution 240,000; maximum injection time 507 ms; normalized AGC 250% | same |
| MS2 | DIA window 68 Da; Orbitrap resolution 240,000; maximum injection time 507 ms; normalized AGC 1000% | same |
| Collision energy | 32% | 28% |
| Scan events | 9 | 6 |
| Loop count | 3 (one MS1 scan after every 3 MS2 scans) | 3, with a loop time of 3 s |

### MS data analysis

- Raw data were analyzed in directDIA+ mode (library-free) in Spectronaut.
  - **Total kidney:** Spectronaut v20.2.250922.92449 against a mouse UniProt database (downloaded on October 7, 2025).
  - **DCT:** the control and zero-K runs were searched together in one search (Spectronaut v21.1.260825.94842; Uniprot_mouse_reviewed_20261013.fasta), so protein inference, FDR filtering and cross-run normalization ran over both conditions (6,208 protein groups).
- Peptide and protein false discovery rates were set at 1%, and quantification was at the MS1 level.
- Acetylation of the protein N-terminus and oxidation of methionine were variable modifications. Carbamidomethylation of cysteine was not set, because the workflow has no alkylation step.
- Cross-run global normalization was enabled, and imputation was not.
- The protein group quantities (PG.Quantity) were exported as CSV files for the analysis below.

## Data analysis

Analyses were done in Python with Scanpy (Wolf et al., *Genome Biol* 2018;19:15). The analysis is at the protein level; gene names are used as protein names throughout.

### Data processing and quality control

- **Filtering:** cells with fewer than 100 detected proteins (protein groups with intensity > 0) were removed first; proteins detected in fewer than two of the retained cells were then removed. The DCT data were filtered separately for each diet condition.

| Data set | Cells sorted | Cells retained | Protein groups retained | Proteins per retained cell |
| --- | --- | --- | --- | --- |
| Total kidney | 768 | 712 | 4,054 of 4,144 | 101 to 2,188 |
| DCT, control | 768 | 729 | 6,078 of 6,208 | 100 to 4,715 |
| DCT, zero-K | 767 | 702 | 5,953 of 6,208 | 105 to 4,466 |

- **Transformation:** no further per-cell normalization was applied. Intensities were ln(1 + x) transformed, and each protein was scaled to zero mean and unit variance (values capped at 10).
- **Missing values:** a protein that was not detected in a cell is kept as not detected; nothing is imputed.
- **Proteins per cell and dynamic range:** proteins per cell were counted among the retained proteins (intensity > 0). The dynamic range within a cell is log<sub>10</sub>(P95/P5) of its non-zero protein intensities (95th and 5th percentiles).

### Dimensionality reduction and clustering

Total kidney cells and each DCT diet condition were analyzed separately.

- **PCA:** principal component analysis on the scaled matrix of all retained proteins.
- **Neighbor graph:** k = 10 nearest neighbors on the top 20 components.
- **UMAP:** the two-dimensional embedding was computed from this graph. Cell-type labels were not used to compute it; they only define the colors of the cells.
- **Clustering:** Leiden clustering (igraph implementation, seed 42) on the same graph, at resolution 2 for total kidney cells and resolution 1 for each DCT diet condition.

### Cluster annotation (cell types)

Clusters were annotated from their differentially expressed proteins and curated marker lists (Supplementary Table S2 of the manuscript: a kidney list with an added endothelial row, and a DCT list).

1. **Differential proteins.** Each cluster was compared with all other cells by a two-sided Wilcoxon rank-sum test on ln(1 + intensity), with missing values set to 0, for the proteins detected in at least 20% of the cluster's cells. P values were adjusted by the Benjamini–Hochberg method within each cluster.
2. **Top list.** Increased proteins had q < 0.05, an area under the curve (AUC) > 0.5 and a positive mean difference. The top list held up to 25 increased proteins ranked by AUC.
3. **Marker enrichment.** For each cell type, enrichment of its markers in the top list was tested by the hypergeometric test (Benjamini–Hochberg correction over all cluster × cell-type tests). The cluster took the cell type with the lowest P value.
4. **Shared markers.** A marker listed for two or more cell types was treated as shared. In the DCT data, Slc12a3 and Umod were treated as shared.
5. **Type-specific marker at any rank.** A cluster whose top list held no marker, or only shared markers, took instead the cell type whose type-specific marker was significantly increased at any rank. If there was none, the cluster kept its shared-marker label or was labeled *Unknown* (in the DCT data: *DCT, subtype not resolved*).
6. **Small clusters.** Clusters of fewer than 5 cells were not annotated.

- **Endothelial row:** Pecam1, Emcn, Eng, Esam, Icam2, Fabp4 and Ehd4 were added to the kidney list after these proteins were found in a cluster of 19 cells in which the macula densa marker Nos1 was not detected. The row was not pre-specified.
- **Resolution scans:** resolutions 0.5–6.0 (total kidney) and 0.3–3.0 (each DCT diet condition) were scanned with Leiden seeds 0–9 in addition to 42, and every clustering was annotated with the same rule.

### Per-cell proliferation test (ProLIF cells, DCT data)

ProLIF cells are called per cell, separately from the cluster annotation. No cluster was annotated as ProLIF.

- **Proliferation set:** the S-phase and G2/M-phase lists of Tirosh et al. were matched to the quantified proteins. The 36 proteins quantified in both conditions, without Mki67 and Top2a, formed the set.
- **Score:** cells were divided into 20 equal-sized bins of the number of proteins identified. For each cell, the score is the mean over the proliferation set of the difference between detection in the cell (1 or 0) and the detection rate of that protein in the cell's bin. A protein that was not detected was treated as not measured.
- **Null:** the same score was computed for 1,000 random sets of 36 proteins, drawn from the retained proteins outside the S and G2/M lists and a cell-cycle panel, and matched to the proliferation set on deciles of detection frequency (seed 42).
- **Call:** the empirical P value was (1 + the number of random sets with a score at or above the observed score) / 1,001, adjusted by the Benjamini–Hochberg method over the cells of the condition. Cells with q < 0.05 were called cycling. Cycling cells in which Slc12a3 (NCC) was detected were labeled ProLIF.
- **Counts:** 37 of 729 control cells and 63 of 702 zero-K cells.
- **Criteria fixed before the test was run:** ProLIF cells were not to be shallower than other cells and not associated with sort plate; Mki67 or Top2a was to be detected more often in ProLIF cells; random protein sets in place of the proliferation set were to give fewer cycling cells; and the ProLIF set was to be stable over 10 other random seeds. All were met in both conditions.

### Comparison of zero-K and control DCT cells

- **Design limit:** control and zero-K cells came from one pool of three mice per condition. Condition and pool cannot be separated, cells are not animal-level replicates, and all P and q values are descriptive.
- **Proteins compared:** the 5,897 protein groups retained in both conditions. The 181 and 56 protein groups retained in control or in zero-K only were listed and not tested.
- **Cell groups:** cells were grouped by the cluster annotation of their condition; the main group was the cells annotated as DCT1 or DCT2.
- **Transferred label:** because no zero-K cluster was annotated as DCT2, each zero-K cell was also given the most frequent cluster annotation of its ten nearest control cells in a principal-component space computed over the cells of both conditions (20 components).
- **Pre-specified panel:** a panel of 22 proteins and six scores was fixed before any comparison between the conditions was tested, with an expected direction under the zero-K diet for eight proteins, taken from published low-potassium studies of whole kidney or cortex. The number of cells with each panel protein detected in each condition was known when the directions were fixed.
- **Two-part test:** for each protein, with the logarithm of the number of proteins detected per cell as a covariate:
  - a Firth-penalized logistic regression for detection;
  - ordinary least squares on ln intensity among the cells with the protein detected, fitted when at least five cells per condition had it detected;
  - the likelihood-ratio statistics of the two parts were summed into one test, with Benjamini–Hochberg correction.
- The same test was applied to all proteins detected in at least 10% of the cells of either condition. The DCT browser shows these stored results; it runs no test of its own.

### Values shown in the browsers

- **Detection rate:** the fraction of a cell type's cells with intensity > 0.
- **Median intensity:** computed over the detected cells only.
- **Mean ln(1 + intensity):** computed over all cells of the cell type, with not-detected cells counted as 0.
- **Marker dotplots:** dot size is the fraction of a group's cells with intensity > 0. Color is the group mean of the per-protein z-scored ln(1 + intensity), rescaled from 0 to 1 per protein across the rows shown.
- **Core and unique proteins:** these use protein detection, not intensity, and both thresholds are sliders in the browsers.
  - *Core* = detected in at least Y% of a cell type's cells.
  - *Unique* = core in at most X% of the other selected cell types.
  - In the manuscript, the core proteome of a cell type holds the proteins detected in at least 50% of its cells, and its unique-core proteome the core proteins detected in less than 10% of the cells of every other type.

## Further analyses in the manuscript

The Supplementary Methods of the manuscript also describe:

- the HeLa benchmark of the LC-MS system and the sample preparation workflow;
- preprocessing sensitivity analyses (per-cell normalization, selection of highly variable proteins and other alternatives to the main pipeline);
- mitochondrial protein metrics, dissociation-stress proteins and quality flags;
- comparisons with the RNA of the Mouse Kidney Atlas and with the proteomes of microdissected rat tubule segments;
- negative markers (Slc12a1, Aqp2) and uromodulin in the DCT data;
- the comparison of the two sort plates of each condition;
- robustness and specificity analyses of the zero-K comparison;
- diffusion pseudotime, cell-cycle correction and aldosterone-response scores in the DCT data;
- the immunofluorescence analysis of kidney sections.

## Data and code

- **Raw data:** ProteomeXchange / PRIDE, PXD073729 (total kidney). The accession of the DCT data will be added on publication.
- **Processed data:** Zenodo (DOI to be added on publication). Each browser also offers its data as downloads.
- **Code:** the Python scripts of the analyses are on GitHub: [github.com/qiwu-au/scp_mouse_kidney_dct](https://github.com/qiwu-au/scp_mouse_kidney_dct).
