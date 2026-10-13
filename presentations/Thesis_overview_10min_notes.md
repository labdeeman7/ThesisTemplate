# Thesis overview: 10-minute speaker notes

Exactly 10 slides; planned speaking time: 10:00.

The thesis sources are authoritative where older decks differ.


## 1. Towards fine-grained surgical scene understanding

0:00–0:30 (30 seconds)

My thesis asks how a system can understand which individual surgical instrument is doing what, and to which tissue. The full thesis title is Towards Fine-Grained Surgical Scene Understanding through Grounded Instrument–Tissue Interaction Modelling. The work moves from a review of surgical vision to instance-level datasets, grounded action models, and finally a two-stage vision–language system. The unifying contribution is spatial grounding of surgical interactions.


## 2. Recognising an action does not identify its actor

0:30–1:30 (60 seconds)

A surgical action triplet consists of an instrument, a verb, and a target: for example, a grasper retracting the liver. Traditional recognition tells us that this interaction occurs somewhere in a frame. But if two graspers appear, it does not identify which one is responsible. Instrument segmentation solves a different part: it tells us where each tool is, but not what it is doing. The rightmost panel joins these two kinds of information. Each interaction is attached to the mask of the responsible instrument instance. That is the task studied throughout this thesis. The target is a semantic anatomical label; this does not mean we have segmented all the tissue.


## 3. The review maps how surgical vision tasks connect

1:30–2:35 (65 seconds)

The PhD began with a broad review of multitask learning in minimally invasive surgical vision. I organised work across perceptual tasks, tracking and camera control, workflow and activity understanding, and post-surgical analysis. These tasks need complementary information: objects, motion, procedural context, and interactions. Multitask learning can learn related outputs together, commonly through a shared encoder and separate heads. However, simply combining tasks does not guarantee improvements. The review identified negative transfer as well as benefits, and found that surgical work often used hard parameter sharing and simple weighted losses. Its contribution is both a map of applications and a critical discussion of how task relationships, optimisation, and annotation availability shape progress.


## 4. The review exposes a missing spatial connection

2:35–3:30 (55 seconds)

The key transition from the review to the rest of the thesis is the gap between semantic richness and spatial evidence. Workflow labels say where we are in an operation. Triplets describe finer actions and anatomical targets. But frame-level triplets still leave the responsible instrument ambiguous. At the same time, large-scale instrument instance annotations for routine laparoscopic surgery were scarce. This points to two connected requirements: distinguish individual instruments, then align the action labels with those instances. Multitask learning remains useful background, but grounding becomes the organising problem of the thesis. The dataset work is therefore essential supervision for the later interaction models, rather than a separate side project.


## 5. CholecInstanceSeg: distinguish individual instruments

3:30–4:35 (65 seconds)

CholecInstanceSeg establishes the spatial foundation. It contains 41,933 annotated frames from 85 procedures, with 64,483 instrument instances. The source videos come from the existing Cholec dataset family, and the annotations add semantic classes and instance identities. To scale the work, annotation is iterative: initialise masks, train a model, generate proposals, review and correct them, and retrain. Human review and quality control remain part of this process. The important advance for the thesis is that repeated or overlapping tools can be distinguished. Dataset limitations include class imbalance and difficult visual conditions. These masks enable the next step: connecting an instrument to its surgical role.


## 6. CholecTriplet-Seg: link masks to surgical interactions

4:35–5:40 (65 seconds)

CholecTriplet-Seg aligns CholecInstanceSeg masks with CholecT50 triplet labels, using manual alignment and quality control. It includes 30,955 frames, 49,866 grounded triplets, and 50 videos. Alignment is particularly important when multiple instruments share a class, or when mask labels and frame-level labels disagree. The prediction target is an instrument mask with its instrument, verb, and target labels. Evaluation checks the spatial match and the semantic labels together. Complete-triplet average precision is therefore demanding: the localisation and all three components must be correct for the same instance. Component scores help diagnose the errors, but they are not substitutes for complete interaction performance.


## 7. TargetFusionNet adds weak anatomical context

5:40–6:45 (65 seconds)

Anatomical target prediction is a principal bottleneck. Tissue is deformable, partially visible, and often difficult to distinguish from local appearance alone. TargetFusionNet extends Mask2Former with a second source of information: coarse anatomy predictions from EndoViT. Gated fusion allows instrument queries to use these predictions as contextual cues. They are weak priors, not reference anatomy annotations, and their categories do not exactly match our target vocabulary. Under mask-based complete-triplet evaluation, the strongly supervised Mask2Former-Triplet baseline reaches 12.23 AP; TargetFusionNet reaches 13.47. The broad lesson is that strong instance supervision is foundational, and anatomical context provides an additional gain in this architecture.


## 8. Two stages separate localisation from interaction prediction

6:45–7:50 (65 seconds)

The final chapter asks whether localisation and interaction prediction can be specialised into separate stages. Stage one uses Mask2Former to segment and classify instruments. The image is then overlaid with the masks and instrument identifiers. Stage two uses Qwen3-VL-8B-Instruct, adapted with supervised fine-tuning, to predict a verb and a target for each supplied instance. The instrument identity is fixed by stage one and cannot be corrected by stage two. The output is structured and linked by instance IDs. I also examine sequential dialogue, short temporal context, anatomical prompts, ontology guidance, and distilled rationale supervision. These alternatives test whether a different task formulation or source of context improves the semantic prediction.


## 9. Better components do not guarantee better complete triplets

7:50–9:10 (80 seconds)

There are two evaluation settings, and it is important not to mix them. With ground-truth instruments supplied, direct supervised fine-tuning achieves 14.56 complete-triplet AP. Sequential dialogue gives 15.31, and three-frame context gives the highest observed score, 15.89. These are exploratory observations, not established significant improvements, and these adaptations were not evaluated in the complete predicted-instance pipeline. With predicted instruments, direct fine-tuning reaches 13.52 AP, essentially comparable to TargetFusionNet at 13.47. Verb and target component scores are higher, as shown in the table, but the complete relationship still needs every element to be correct together. Five-frame context and rationale-only supervision do not improve the result in the tested formulations. More context or longer generated explanations therefore does not automatically help.


## 10. Grounding makes surgical interactions spatially explicit

9:10–10:00 (50 seconds)

The take-home message is that recognising an interaction is not the same as identifying its actor. This thesis connects the two by providing instrument instance annotations, aligning them with triplets, and developing both target-aware and two-stage models. The review motivates this progression and gives the broader surgical-vision context. The main remaining challenge is robust target prediction and consistent complete-triplet assignment. Limitations include class imbalance, visual ambiguity, dependence on first-stage masks, and evaluation restricted to laparoscopic cholecystectomy. Next steps are temporal instance association, evaluation of the promising adaptations with predicted instruments, and testing across other procedures. The work provides a research foundation for interpretable surgical scene understanding; downstream clinical applications still need their own validation.