# Labeling Candidate Pack

These are candidate queries and likely matching papers from lexical search.
They are not ground truth. Review the abstracts before copying IDs into labels.

## Candidate 001

Query: retrieval augmented generation for factual question answering

Likely paper IDs:

1. `2606.10381v1` score=0.3083
   Title: Agentic Hybrid RAG for Evidence-Grounded Muon Collider Analysis
   Categories: hep-ex, cs.AI, cs.CL, cs.IR, physics.ins-det
   Abstract: Muon collider research spans accelerator physics, detector instrumentation, and high-energy phenomenology, with relevant evidence scattered across a rapidly expanding and heterogeneous body of scientific literature. As high-energy physics (HEP) increasingly explores agent-assisted analysis workflows, efficiently locating, integrating, and verifying scientific evidence becomes an essential capability. While retrieval-augmented generation (RAG) offers a promising framework for scientific question answering, integrating agentic reasoning without compromising retrieval precision remains a key challenge. In this work, we present agentic hybrid RAG, an evidence-grounded RAG framework for muon coll...

2. `2606.11945v1` score=0.2567
   Title: uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking
   Categories: cs.CL, cs.IR
   Abstract: This report describes our participation in SemEval-2026 Task 8 on multi-turn retrieval and question answering. The task evaluates conversational systems across four domains (finance, cloud documentation, government, Wikipedia), and includes unanswerable queries where the available collection does not contain sufficient evidence to produce a complete response. We propose a multi-turn retrieval-augmented generation pipeline that combines learned sparse retrieval with LLM-based reranking and generation. Using sparse retrieval as the primary retrieval method, we leverage its strong generalization across domains. In addition, we make use of the long-context capabilities of LLMs for conversational...

3. `2606.18103v1` score=0.2325
   Title: HistoRAG: Embedding Historical Methodology in Retrieval-Augmented Generation Through Critical Technical Practice
   Categories: cs.CL, cs.IR
   Abstract: Retrieval-Augmented Generation (RAG) is the prevailing architecture for grounding language model outputs in external evidence, yet its dominant evaluation paradigms and default configurations remain oriented toward factual question-answering. For interpretive disciplines such as historical studies, RAG embeds assumptions that conflict with scholarly practice. We introduce HistoRAG, a framework that translates historiographical principles into concrete architectural interventions. Separated retrieval and generation decouples source discovery from interpretation, temporal windowing enforces balanced source representation across the research period as a methodological requirement of historical ...

4. `2606.15741v1` score=0.1901
   Title: A Self Consistency Based Reranking for Narrative Question Answering
   Categories: cs.CL, cs.AI
   Abstract: Narrative question answering (NQA) is a challenging task in natural language processing that requires models to understand long textual contexts, capture relationships across events, and generate coherent responses. Despite recent advances in pretrained language models, most existing approaches rely on a single decoding output during inference, making them sensitive to generation variability and often resulting in incomplete or inconsistent answers .To address this limitation, we propose a self-ensemble Self-Consistency-Based reranking framework for narrative question answering. The proposed method generates multiple candidate answers for each story-question pair and selects the final answer...

5. `2606.07924v1` score=0.1821
   Title: Decoupling Semantics and Logic: A Training-Free Coarse-to-Fine Pipeline for Video Retrieval-Augmented Generation
   Categories: cs.CV, cs.AI, cs.CL, cs.LG, cs.MM
   Abstract: This paper presents our system description for the 2nd Workshop on Multimodal Augmented Generation via MultimodAl Retrieval (MAGMaR). Addressing the critical challenges of cross-lingual long-video comprehension, strict persona adherence, and zero-hallucination temporal grounding, we propose a fully training-free, two-stage cascaded Video RAG pipeline. Our architecture strategically decouples semantic retrieval from cognitive logical reasoning through a modality-aware division of labor. In the first stage, a high-recall semantic pre-fetching module employs dense retrieval using only high-fidelity visual summaries and global text descriptions, explicitly isolating noisy modalities (e.g., OCR a...

6. `2606.19759v1` score=0.1785
   Title: Optimal Scheduling in a Question-Answering Forum of Knowledge Workers
   Categories: cs.AI, cs.SI
   Abstract: As individuals turn to the Internet to find answers to questions they may have, several Question Answering (QA) forums have evolved, where users knowledgeable in certain topics can contribute their expertise to answering these requests for information. While these are currently volunteer based, we consider a future version employing knowledge workers who are experts in certain topics. In such a system, the request-answer processes forming the queuing system may utilize schedulers that assign requests in different topics to the experts in the forum, who may be able to answer them according to their expertise levels in different topics. With this model, we calculate the capacity of the system ...

7. `2606.13680v1` score=0.1783
   Title: Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning
   Categories: cs.CL, cs.AI
   Abstract: Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly suited for complex reasoning tasks: a semantically similar problem may demand an entirely different solution strategy, while a superficially different problem may share the same underlying reasoning pattern. We propose Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT), a post-training framework that teaches language models to reason by analogy. RA-RFT uses gold-relevance distillation to train a retriever that ranks contexts by expected reasoning benefit rather than semantic overlap, and then...

8. `2606.15861v1` score=0.1774
   Title: Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   Categories: cs.CV
   Abstract: Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, with the potential to support surgical training and intraoperative decision-making. Recent Vision-Language Models (VLMs) have shown promising performance through parameter-efficient fine-tuning; however, most existing approaches rely on coarse visual grounding, typically limited to bounding boxes, which fails to capture the fine-grained spatial structure of surgical objects. In this work, we propose a unified framework that jointly performs pixel-level segmentation and visual question an...


## Candidate 002

Query: multi turn retrieval augmented generation with reranking

Likely paper IDs:

1. `2606.11945v1` score=0.5168
   Title: uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking
   Categories: cs.CL, cs.IR
   Abstract: This report describes our participation in SemEval-2026 Task 8 on multi-turn retrieval and question answering. The task evaluates conversational systems across four domains (finance, cloud documentation, government, Wikipedia), and includes unanswerable queries where the available collection does not contain sufficient evidence to produce a complete response. We propose a multi-turn retrieval-augmented generation pipeline that combines learned sparse retrieval with LLM-based reranking and generation. Using sparse retrieval as the primary retrieval method, we leverage its strong generalization across domains. In addition, we make use of the long-context capabilities of LLMs for conversational...

2. `2606.11265v1` score=0.3265
   Title: When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines
   Categories: cs.CR, cs.AI
   Abstract: Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection. Existing studies mainly evaluate poisoning under simplified retrieval settings, overlooking practical RAG pipelines involving document chunking, dense retrieval, reranking, and grounded generation. In this paper, we revisit corpus poisoning under realistic multi-stage retrieval pipelines and show that many existing attacks substantially degrade after reranking despite achieving high retrieval-stage relevance. We identify retrieval granularity mismatch as a key reason for this failure: document-level adversarial signals are oft...

3. `2606.09169v1` score=0.2465
   Title: IMUG-Bench: Benchmarking Unified Multimodal Models on Interleaved Understanding and Generation
   Categories: cs.AI, cs.CV, cs.MM
   Abstract: In recent years, unified multimodal models (UMMs) have emerged to support both understanding and generation within a single framework. Mastering dynamic, multi-turn interleaved image-text dialogues is a crucial task for UMMs in real-world applications. However, existing benchmarks fail to evaluate this important task, as they are often limited to single-turn or static settings, and typically overlook exposure bias in multi-turn interactions. To bridge this gap, we propose IMUG-Bench, a comprehensive benchmark for multi-turn interleaved image-text dialogue of UMMs that jointly evaluates their understanding and generation capabilities. Our IMUG-Bench comprises three classes: Static Spatial, Te...

4. `2606.07924v1` score=0.2429
   Title: Decoupling Semantics and Logic: A Training-Free Coarse-to-Fine Pipeline for Video Retrieval-Augmented Generation
   Categories: cs.CV, cs.AI, cs.CL, cs.LG, cs.MM
   Abstract: This paper presents our system description for the 2nd Workshop on Multimodal Augmented Generation via MultimodAl Retrieval (MAGMaR). Addressing the critical challenges of cross-lingual long-video comprehension, strict persona adherence, and zero-hallucination temporal grounding, we propose a fully training-free, two-stage cascaded Video RAG pipeline. Our architecture strategically decouples semantic retrieval from cognitive logical reasoning through a modality-aware division of labor. In the first stage, a high-recall semantic pre-fetching module employs dense retrieval using only high-fidelity visual summaries and global text descriptions, explicitly isolating noisy modalities (e.g., OCR a...

5. `2606.12941v2` score=0.2247
   Title: Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL
   Categories: cs.CL
   Abstract: When a user reveals task-critical information across several conversation turns, LLM accuracy drops by up to 65% despite full context availability. We show that this Lost in Conversation degradation can be substantially mitigated by training models to maintain a compact rolling memory instead of attending to a growing history. To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation. Training only on sharded GSM8K, our memory-augmented policy significantly improves multi-turn accuracy and generalises zero-shot to harder math and out-of-do...

6. `2606.10740v2` score=0.2124
   Title: When the Chain of Thought Knows Better: Failure Modes in Multi-Turn Reasoning Models
   Categories: cs.AI, cs.CL, cs.LG
   Abstract: Failures in multi-turn reasoning models are largely invisible to terminal-score evaluation. A model can lock onto an unsafe stance early in a long dialogue, yet its final-turn refusal rate may appear indistinguishable from a robustly aligned baseline. To expose these hidden temporal dynamics, we propose a trace-level diagnostic - the CoT-Output 2x2 safety matrix. This framework labels every turn along two independent axes (internal reasoning and visible output), yielding four operationally defined failure cells: robust alignment, alignment faking, overt jailbreak, and a distinct failure mode we term context-injection failure (where the CoT maintains safe reasoning, but the visible output pro...

7. `2606.15741v1` score=0.2028
   Title: A Self Consistency Based Reranking for Narrative Question Answering
   Categories: cs.CL, cs.AI
   Abstract: Narrative question answering (NQA) is a challenging task in natural language processing that requires models to understand long textual contexts, capture relationships across events, and generate coherent responses. Despite recent advances in pretrained language models, most existing approaches rely on a single decoding output during inference, making them sensitive to generation variability and often resulting in incomplete or inconsistent answers .To address this limitation, we propose a self-ensemble Self-Consistency-Based reranking framework for narrative question answering. The proposed method generates multiple candidate answers for each story-question pair and selects the final answer...

8. `2606.13544v1` score=0.1785
   Title: Adaptive Turn-Taking for Real-time Multi-Party Voice Agents
   Categories: eess.AS, cs.AI, cs.CL
   Abstract: Turn-taking in multi-party spoken conversations remains a fundamental challenge for voice-based agents, particularly under dynamic floor competition and varying user expectations. We propose ModeratorLM, a role-playing voice agent that conditions turn-taking behavior on an explicitly assigned role in multi-party settings. The system is built on a speech large language model operating in chunk-wise streaming manner. We further introduce a reasoning-augmented variant that incorporates chain-of-thought reasoning over conversational context and the assigned role. We construct RolePlayConv, a large-scale synthetic dataset of spoken multi-party conversations with diverse assistant roles. Experimen...


## Candidate 003

Query: hallucination detection and factuality evaluation in large language models

Likely paper IDs:

1. `2606.08831v1` score=0.4033
   Title: Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models
   Categories: cs.AI
   Abstract: Large language models (LLMs) increasingly perform multi-step reasoning, where intermediate claims form implicit directed acyclic graphs whose node correctness is structurally conditioned on their ancestors. This makes factuality uncertainty structural, rather than a trivial accumulation of node-wise errors, and necessitates inference-time uncertainty quantification over the reasoning structure. While conformal prediction (CP) offers flexible user-specified factuality control, existing work remains post-hoc and cannot intervene during generation. To fill the gap between CP's flexibility and its post-hoc limitation, we propose an \emph{Inference-Time Conformal Reasoning (ITCR)} framework that ...

2. `2606.08158v1` score=0.3026
   Title: Constrained Paraphrase Consistency for LLM Hallucination Detection
   Categories: cs.CL, cs.AI
   Abstract: Large language models (LLMs) can generate factually inconsistent claims, motivating accurate and scalable hallucination detectors. Prior work largely enlarges training sets via synthesis or new annotations, introducing increasing cost and potential bias while underusing the consistency implied by semantically equivalent paraphrases. We propose Consistency-Constrained Hallucination Detector (CCHD), which formulates training as a constrained optimization problem. The standard cross-entropy on original document-claim pairs is complemented by (i) paraphrase-consistency constraints bounding divergence across paraphrased views, and (ii) label-preservation constraints tying paraphrases to ground tr...

3. `2606.18609v1` score=0.2417
   Title: Hallucination Detection and Correction in Medical VLMs via Counter-Evidence Verification
   Categories: cs.CV
   Abstract: Vision-Language models (VLMs) reliability in medical diagnosis is challenged by trust-undermining hallucinations. Existing hallucination detection approaches mainly focus on identifying factual inconsistencies between generated text and reference data. While some studies analyze where models attend in images, they seldom verify whether such attention truly reflects the visual evidence supporting the generated text. To address this gap, we propose Co}unter-Evidence Verification (CoEV), a training-free plug-and-play framework that detects and corrects hallucinations through evidence-based factual consistency verification. CoEV performs bidirectional verification between textual assertions and ...

4. `2606.12900v1` score=0.2077
   Title: Zero-source LLM Hallucination Detection with Human-like Criteria Probing
   Categories: cs.AI, cs.CL, cs.LG
   Abstract: Large language models (LLMs) often hallucinate by generating factually incorrect or unfaithful content, posing significant risks to their safe use. Detecting such hallucinations is particularly challenging under the zero-source constraint, where no model internals or external references are available, and detection must rely solely on the textual query-answer pair. In this paper, we propose Human-like Criteria Probing for Hallucination Detection (HCPD), a paradigm that emulates the multi-faceted reasoning of human evaluators. Its core is a Human-like Criteria Probing (HCP) mechanism, in which a LLM agent adaptively decomposes its judgment into a weighted set of interpretable criteria and agg...

5. `2606.08000v1` score=0.2063
   Title: Summarization is Not Dead Yet
   Categories: cs.CL, cs.AI
   Abstract: The progress of large language models (LLMs) has fueled claims that model-generated summaries rival or even surpass human-written references, raising questions about whether summarization remains an open research problem. We re-examine this narrative through a multi-track evaluation covering five diverse datasets and five state-of-the-art LLMs, combining controlled human assessment, bias-mitigated LLM-as-Judge protocols, factuality verification against external knowledge, and corpus-level linguistic analysis. Our findings reveal a more nuanced landscape in which human reference summaries continue to demonstrate advantages in informativeness and faithfulness, whereas LLM outputs are preferred...

6. `2606.13211v1` score=0.1959
   Title: Hallucination in Medical Imaging AI: A Cross-Modality Analytical Framework for Taxonomy, Detection, and Mitigation under Regulatory Constraints
   Categories: cs.AI
   Abstract: AI systems are being deployed across medical imaging faster than their failure modes are understood. At this point in time, the failure of greatest clinical concern is hallucination: clinically plausible but factually incorrect outputs, including fabricated anatomical structures, missed findings, incorrect laterality, and invented measurements in generated reports, with direct consequences, for example, for biopsy decisions, staging, and treatment planning. This structured narrative synthesizes peer-reviewed studies, benchmark datasets, and FDA regulatory guidance across five imaging modalities to produce a cross-modality analysis of hallucination taxonomy, etiology, detection, and mitigatio...

7. `2606.08705v1` score=0.1925
   Title: Analyzing the Correlation Between Hallucinations and Knowledge Conflicts in Large Language Models
   Categories: cs.CL
   Abstract: Hallucinations -- factually incorrect or unverifiable outputs -- remain one of the most challenging limitations of Large Language Models (LLMs), especially in knowledge-intensive tasks. One proposed explanation is internal knowledge conflicts arising from fixed, outdated training data. This paper investigates whether internal representations linked to knowledge conflicts correlate with hallucination behaviors in LLMs. Using probing techniques inspired by two prior works, we analyzed activations from hidden, attention, and MLP layers, as well as output logits, across predefined tasks. We probed LLaMA-3-8B on hallucination detection benchmarks and Falcon-7B on a knowledge conflict dataset. Our...

8. `2606.12476v2` score=0.1903
   Title: Quickest Detection of Hallucination Onset: Delay Bounds and Learned CUSUM Statistics
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: Token-level hallucination detectors are evaluated as classifiers, by AUC over all tokens, yet a streaming monitor is judged by its reaction time: the number of tokens that pass between the onset of a hallucination and the alarm. We formulate hallucination onset detection as a quickest change detection problem. A first-order Markov model of the latent faithful/hallucinated state, validated on RAGTruth, places the task inside classical change-point theory and yields Lorden's lower bound on detection delay: about 1.3 tokens at a false-alarm rate of 0.01. We then show that a causal recurrent labeler acts as a CUSUM with a learned increment. Among the onsets it catches it detects in 11-13 tokens,...


## Candidate 004

Query: LLM agents for scientific literature analysis

Likely paper IDs:

1. `2606.12736v1` score=0.3930
   Title: Benchmarking AI Agents for Addressing Scientific Challenges Across Scales
   Categories: cs.AI, cs.LG
   Abstract: AI agents are increasingly being developed to accelerate scientific discovery, yet their practical capabilities in real research settings remain poorly understood. Existing benchmarks for AI agents rarely capture the complexity, heterogeneity, and extended reasoning required by scientific work, whereas benchmarks for scientific tasks often reduce research to static, direct problems and provide limited support for interactive evaluation. Here, we introduce SciAgentArena, a systematic benchmark for evaluating AI agents in real-world scientific research scenarios drawn from emerging needs across multiple domains. SciAgentArena comprises approximately 200 tasks with stepwise verification and an ...

2. `2606.10381v1` score=0.2688
   Title: Agentic Hybrid RAG for Evidence-Grounded Muon Collider Analysis
   Categories: hep-ex, cs.AI, cs.CL, cs.IR, physics.ins-det
   Abstract: Muon collider research spans accelerator physics, detector instrumentation, and high-energy phenomenology, with relevant evidence scattered across a rapidly expanding and heterogeneous body of scientific literature. As high-energy physics (HEP) increasingly explores agent-assisted analysis workflows, efficiently locating, integrating, and verifying scientific evidence becomes an essential capability. While retrieval-augmented generation (RAG) offers a promising framework for scientific question answering, integrating agentic reasoning without compromising retrieval precision remains a key challenge. In this work, we present agentic hybrid RAG, an evidence-grounded RAG framework for muon coll...

3. `2606.13020v1` score=0.2653
   Title: SciR: A Controllable Benchmark for Scientific Reasoning in LLMs
   Categories: cs.AI
   Abstract: Three paradigmatic forms of inference recur across scientific reasoning: deduction, induction, and causal abduction. Reliably evaluating LLMs on these in scientific settings is currently out of reach: scientific benchmarks built on human annotations are costly and lack mechanistic ground truth, while synthetic logical-reasoning benchmarks do not resemble real scientific documents. We introduce SciR, a benchmark that combines multi-paradigm reasoning with controllable scientific rendering, anchored on three paradigmatic scientific problems. Tasks are generated from formal objects (deduction tree, inductive rule hypothesis, causal graph) to guarantee verifiable answers, then rendered into mult...

4. `2606.07718v1` score=0.2526
   Title: A case study of evaluating AI agents on a neuroscience data-to-discovery pipeline
   Categories: cs.AI, cs.CV, cs.LG
   Abstract: Agentic AI tools offer a promising path to automating software development bottlenecks in scientific research pipelines, particularly for stages that take domain experts days to months to build, where scientists care about correctness and robustness, not implementation details. We present an empirical study of general-purpose coding agents on a fly optogenetics data-to-discovery pipeline. We assess agents on tasks substantially larger than existing benchmarks, datasets orders of magnitude bigger, and evaluation criteria grounded in domain expert standards. We show that agents can solve several individual pipeline stages, suggesting stage-level automation is tractable. By analyzing agents' co...

5. `2606.13669v1` score=0.2512
   Title: Agents-K1: Towards Agent-native Knowledge Orchestration
   Categories: cs.AI
   Abstract: Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions, and flat \texttt{cites} edges, omitting key entities, claims, evidence, mechanisms, and method lineages essential for scientific reasoning. To this end, we introduce \textbf{Agents-K1}, an end-to-end knowledge orchestration pipeline that converts raw documents into agent-native scientific knowledge graphs. Agents-K1 integrates three components under a unifying theoretical foundation: a multimodal parser whose five-module schema captures entities, multimodal evidence, citations, and typed inter-...

6. `2606.09105v3` score=0.2340
   Title: Graph2Idea:Retrieval-Augmented Scientific Idea Generation with Graph-Structured Contexts
   Categories: cs.AI
   Abstract: Generating novel, feasible, and high-quality research ideas is an important yet challenging task in scientific discovery. Recent Large Language Model (LLM)-based methods often ground idea generation with retrieved literature, but the retrieved evidence is usually provided as flat text, such as titles, abstracts, or summaries. Such flat contexts may contain redundant or weakly relevant information, while making cross-paper relations among problems, methods, mechanisms, and findings difficult to identify and trace. To address this challenge, we propose Graph2Idea, a knowledge graph-guided framework for retrieval-augmented scientific idea generation.Graph2Idea first retrieves papers according t...

7. `2606.08532v2` score=0.2188
   Title: DN-Hypo-Pipeline: An AI-Driven Workflow for Hypothesis Generation via Large Language Models and Scientific Explanations
   Categories: cs.AI
   Abstract: A scientific hypothesis is the first step in research and undergoes experimental validation, yet it also reflects a deep understanding of and reasoning about scientific phenomena. We introduce DN-Hypo-Pipeline, an AI-powered workflow based on large language models, designed to support structured scientific thinking and hypothesis generation by leveraging scientific explanations as prior knowledge. This pipeline assists researchers in deriving novel hypotheses from existing literature. Given the explanandum (i.e., the conclusion) of a research paper, it identifies underlying laws, theories, and principles, and reconstructs a new, yet-to-be-verified explanation for the observed phenomenon. We ...

8. `2606.11337v1` score=0.2092
   Title: Can AI Agents Synthesize Scientific Conclusions?
   Categories: cs.AI, cs.CL, cs.CY
   Abstract: Scientific AI agents increasingly retrieve evidence, reason across sources, and synthesize conclusions used in consequential decisions. Yet, their ability to do so in high-stakes domains such as health remains unclear. We introduce SciConBench, a large-scale live benchmark of 9.11K questions and expert-written conclusions from systematic reviews to evaluate open-domain scientific conclusion synthesis. The benchmark draws on an expert-validated automated evaluation pipeline that decomposes conclusions into atomic facts and measures correctness and comprehensiveness via factual precision and recall. To mitigate data leakage, we further introduce SciConHarness, a clean-room evaluation harness t...


## Candidate 005

Query: multimodal reasoning benchmark for vision language models

Likely paper IDs:

1. `2606.09585v1` score=0.3656
   Title: Optical Reasoning: Rethinking Images as an Expressive Reasoning Medium Beyond Text
   Categories: cs.AI
   Abstract: Chain-of-Thought (CoT) improves the performance of Large Language Models (LLMs) and has been extended to Multimodal Large Language Models (MLLMs). More recent work further moves from text-based multimodal reasoning toward interleaved-modal reasoning, where intermediate steps can incorporate both textual rationales and visual evidence. In this work, we propose a bolder and more ambitious idea: could images alone serve as the reasoning medium for both language and multimodal tasks? To explore this, we propose optical reasoning, which treats images as a standalone reasoning medium. We instantiate this concept with two variants: typographic-based optical reasoning, which optimizes visual layouts...

2. `2606.11470v1` score=0.3471
   Title: The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes
   Categories: cs.CL
   Abstract: Large Language Models (LLMs) have achieved strong performance across natural language processing tasks, yet reliable reasoning remains an open challenge. Although modern LLMs show progress in structured inference, multi-step problem solving, and contextual understanding, their reasoning behavior is often inconsistent and sensitive to prompting strategies, task design, and model scale. This survey provides a systematic analysis of more than 300 recent papers from arXiv, Semantic Scholar, Google Scholar, Papers with Code, and the ACL Anthology to examine how reasoning capabilities emerge in LLMs and where they fail. We make three main contributions. First, we introduce a structured taxonomy of...

3. `2606.07962v1` score=0.3232
   Title: ChronoPhyBench: Do MLLMs Truly Understand the World or Merely Exploit Language Priors?
   Categories: cs.CV
   Abstract: Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated remarkable proficiency in open-world reasoning and understanding. However, a critical ambiguity persists: it remains unclear whether these models genuinely synthesize cross-modal information to construct physically grounded reasoning chains, or if they merely exploit strong language priors to mask single-modality reliance, thereby hallucinating advanced multimodal capabilities. Motivated by this, and to rigorously mitigate language modality bias and shortcuts, we propose a novel multimodal Chrono}logical Physical Dynamics Reasoning Benchmark ChronoPhyBench, which unifies next state prediction with Visual Questi...

4. `2606.10833v1` score=0.3136
   Title: Do VLMs Reason Like Engineers? A Benchmark and a Stage-wise Evaluation
   Categories: cs.AI
   Abstract: Vision-Language Models (VLMs) demonstrate strong performance on general multimodal reasoning benchmarks, yet their ability to perform engineering reasoning remains largely unexplored. Unlike general visual question answering, engineering problem solving requires interpreting technical diagrams, selecting governing physical principles, and maintaining physically consistent multi-step reasoning. These capabilities are increasingly important for AI systems used in engineering education, scientific assistance, and technical decision-making, where reasoning failures may produce physically invalid yet superficially plausible solutions. Existing benchmarks primarily evaluate final answers and provi...

5. `2606.09148v1` score=0.2952
   Title: Explicit Representation Alignment for Multimodal Sentiment Analysis
   Categories: cs.CL
   Abstract: Multimodal affective analysis aims to understand human sentiment and emotion by jointly modeling heterogeneous modalities such as text and images. However, multimodal models often fail to consistently outperform strong text-only baselines, with performance varying significantly across fusion strategies. In this work, we identify representation misalignment between independently pretrained modality encoders as a key bottleneck for effective multimodal learning, and show through controlled experiments that alignment prior to fusion is often more important than fusion complexity. To address this issue, we propose a unified multimodal affective analysis framework that leverages vision-language m...

6. `2606.15160v1` score=0.2924
   Title: DLWM: Diverse Latent World Models for Efficient Multimodal Reasoning
   Categories: cs.CV, cs.LG
   Abstract: Reasoning capabilities of multimodal large language models (MLLMs) have improved considerably in recent years. Existing approaches typically rely on explicit chain-of-thought or continuous latent-space trajectories to enhance multi-step reasoning. However, these methods generally assume that an input admits a single latent interpretation and unfold reasoning along a fixed path or under a uniform computation budget. In real-world multimodal settings, visual observations are often subject to occlusion, blur, viewpoint variation, or semantic ambiguity, giving rise to multiple plausible interpretations. A uniform reasoning strategy not only limits the model's ability to explore multiple hypothes...

7. `2606.07861v1` score=0.2767
   Title: The Last Visible Pixel: Probing Fine-Scale Perception in Vision-Language Models
   Categories: cs.CV, cs.AI
   Abstract: Recent vision-language models (VLMs) excel at multimodal understanding and reasoning, yet their fine-grained visual perception remains underexplored. A natural extension of ``How many r are there in Strawberry?'' asks: how small a visual pattern can a VLM reliably perceive? As such, we introduce FineSightBench, a new benchmark that systematically probes this limit by separating perception tasks (pixel-level recognition of letters, shapes, objects) from reasoning tasks (spatial reasoning, counting, ordering over small targets) across controlled scales of 4--48px. Through comprehensive experiments and detailed failure mode analysis on state-of-the-art models, we reveal a sharp dissociation: pe...

8. `2606.07402v1` score=0.2726
   Title: M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions
   Categories: cs.CL
   Abstract: Language agents are increasingly deployed over accumulating multimodal information, yet existing benchmarks assume a human-human form with sparse visuals and straightforward content, evaluating neither reasoning over authentic multimodal file interaction nor the interpretation of concealed user information. We therefore introduce M$^3$Exam, a query-centric multimodal conversational memory benchmark built on realistic user-agent interaction, with multi-dimensional evaluation spanning cross-modal grounding and implicit information inference. Benchmarking MLLMs and memory systems reveals persistent gaps in cross-modal grounding, cross session reasoning, and the efficiency cost of accumulating m...


## Candidate 006

Query: video retrieval augmented generation and temporal grounding

Likely paper IDs:

1. `2606.15320v1` score=0.3715
   Title: Conditional Multi-Event Temporal Grounding in Long-Form Video
   Categories: cs.CV
   Abstract: Multimodal large language models have made rapid progress in video temporal grounding, yet real-world applications routinely require localizing every event that satisfies compositional temporal and spatial conditions. Existing benchmarks fall short: they localize only a single moment per query, count without temporal conditions, or treat grounding and counting as disjoint tasks. We introduce CoMET-Bench for Conditional Multi-Event Temporal Grounding in long-form video, comprising 2789 queries over 600 videos averaging 33.8 minutes across five real-world domains, with each query composed from 4 temporal conditions, 3 spatial conditions, and a dedicated negative-query subset. We further propos...

2. `2606.07924v1` score=0.3294
   Title: Decoupling Semantics and Logic: A Training-Free Coarse-to-Fine Pipeline for Video Retrieval-Augmented Generation
   Categories: cs.CV, cs.AI, cs.CL, cs.LG, cs.MM
   Abstract: This paper presents our system description for the 2nd Workshop on Multimodal Augmented Generation via MultimodAl Retrieval (MAGMaR). Addressing the critical challenges of cross-lingual long-video comprehension, strict persona adherence, and zero-hallucination temporal grounding, we propose a fully training-free, two-stage cascaded Video RAG pipeline. Our architecture strategically decouples semantic retrieval from cognitive logical reasoning through a modality-aware division of labor. In the first stage, a high-recall semantic pre-fetching module employs dense retrieval using only high-fidelity visual summaries and global text descriptions, explicitly isolating noisy modalities (e.g., OCR a...

3. `2606.12300v1` score=0.3236
   Title: Natural-Language Temporal Grounding in Hour-Long Videos is a Search Problem: A Benchmark and Empirical Decomposition
   Categories: cs.CV, cs.AI
   Abstract: Temporal grounding--returning the interval $[t_s, t_e]$ for a natural-language query over a video--is the language interface to long-form video, yet has been studied on short videos; the dynamics of hour-scale natural-language grounding remain underexplored. We take the position that at hour-scale, the binding constraint is search, not recognition: Video-LLMs are bottlenecked not by localizing a nearby event, but--given a natural-language query--by searching for the relevant region of a long video. To test this, we release ExtremeWhenBench, the first open hour-scale grounding benchmark (2,273 queries over 194 videos, mean 75.7 min, max 9 hr) with an open-form query distribution. Every open V...

4. `2606.18702v1` score=0.3097
   Title: UniTemp: Unlocking Video Generation in Any Temporal Order via Bidirectional Distillation
   Categories: cs.CV
   Abstract: Autoregressive video diffusion models have emerged as a promising approach for long video generation, achieving strong performance in streaming settings. However, existing methods are restricted to forward temporal generation, whereas practical video creation often requires flexible generation order, e.g., conditioning on future context to extend backward, or on both past and future context for inbetween generation. We bridge this gap by training an autoregressive model that supports generation in arbitrary temporal directions. A key technical challenge arises from the Causal 3D VAE widely used in video diffusion models, which encodes latents strictly conditioned on past context. While suite...

5. `2606.08436v2` score=0.2910
   Title: CACR:Reinforcing Temporal Answer Grounding in Instructional Video via Candidate-Aware Causal Reasoning
   Categories: cs.CV
   Abstract: The task of temporal answer grounding in instructional video (TAGV), which aims to locate precise video segments that respond to natural language queries, is increasingly important for direct video answer retrieval. This task remains challenging due to the need to comprehend semantically complex questions and to address the significant length mismatch between untrimmed videos and short target moments. Existing methods often suffer from sensitivity to irrelevant content or insufficient visual reasoning capabilities. To tackle these limitations, we propose a Candidate-Aware Causal Reasoning (CACR) framework. Our approach first employs a Visual-Language Pre-training based Candidate Selection (V...

6. `2606.08780v1` score=0.2671
   Title: Beyond Consistency: Preserving Temporal Structure in Zero-Shot Video Editing
   Categories: cs.CV
   Abstract: Existing zero-shot video editing methods rely on pre-trained diffusion models, successfully achieving spatial control and basic temporal consistency but fundamentally fail to preserve the video's original temporal structure.This distinction is critical: temporal consistency ensures visual smoothness, but temporal structure dictates the video's high-level narrative, rhythm, and semantic flow. Without this preservation, the edited output, especially for long videos with complex semantic variations, becomes narratively incoherent and semantically ambiguous. To address this limitation, we introduce a novel zero-shot editing approach that, for the first time, explicitly focuses on preserving the ...

7. `2606.10183v1` score=0.2534
   Title: Making Time Editable in Video Diffusion Transformers
   Categories: cs.CV, cs.AI, cs.MM
   Abstract: Modern Diffusion Transformers for video generation provide limited control over the progression of time and the editing of temporal dynamics. We propose a temporal-control methodology that extends a pretrained DiT with explicit time editing, allowing control over motion speed and temporal structure without redesigning the backbone. Its core implementation augments the pretrained model with a lightweight temporal module, preserving the original generative prior while expanding its controllable dynamic range.

8. `2606.14317v1` score=0.2517
   Title: CausalMotion: Structured Physical Reasoning as Keyframe and Trajectory Guidance for Training-Free Video Generation
   Categories: cs.CV
   Abstract: Recent advances in diffusion-based video generation have significantly improved visual quality and short-term temporal coherence. However, existing methods still struggle to produce videos with physically consistent and causally plausible dynamics, especially in scenarios involving long-horizon interactions. This limitation arises from the fact that video diffusion models primarily learn physical consistency implicitly, while vision-language models can directly model physical laws. Based on this idea, in this work, we propose \textbf{CausalMotion}, a training-free framework that injects explicit physical reasoning into video generation through structured intermediate representations. Our key...


## Candidate 007

Query: diffusion model for 3D generation

Likely paper IDs:

1. `2606.09273v1` score=0.4469
   Title: EditSSC: Toward Editable Semantic Occupancy Scenes with Unconditional Diffusion Models
   Categories: cs.CV
   Abstract: 3D semantic scene generation is crucial for autonomous driving applications, yet most methods rely on complex 3D-specific architectures such as triplane encoders and adapted diffusion networks, limiting both their simplicity and their editing capabilities. We propose EditSSC, an editing-ready method for 3D semantic scene generation using 2D Bird's Eye View (BEV) representations and off-the-shelf latent diffusion network. Our approach reshapes 3D semantic occupancy grids into multi-channel BEV images and leverages the quantized autoencoder and UNet from Stable Diffusion with minimal modifications. We perform diffusion on the latents after quantization, which enables training-free editing capa...

2. `2606.13364v1` score=0.3822
   Title: VideoMDM: Towards 3D Human Motion Generation From 2D Supervision
   Categories: cs.LG, cs.CV
   Abstract: We introduce VideoMDM, a diffusion-based framework that trains 3D human motion priors directly from accurate 2D poses extracted from monocular videos, without any 3D ground truth. A pretrained 2D-to-3D lifter provides approximate 3D pose sequences that serve as a noisy teacher: these are diffused, denoised by the model in 3D, and supervised in 2D by reprojecting the prediction and comparing against accurate keypoints. We show that, under mild assumptions, a depth-weighted 2D reprojection loss is equivalent in expectation to direct 3D supervision, and we adapt standard 3D motion regularizers - velocity consistency and over-parameterized representation alignment - to this 2D setting. Unlike me...

3. `2606.10478v1` score=0.3615
   Title: 3D-CoS: A New 3D Reconstruction Paradigm Based on VLM Code Synthesis
   Categories: cs.CV
   Abstract: Most recent 3D reconstruction and editing systems operate on implicit and explicit representations such as NeRF, point clouds, or meshes. While these representations enable high-fidelity rendering, they are fundamentally low-level and hard to control programmatically. In contrast, we propose and systematically evaluate a new 3D reconstruction paradigm, 3D Code Synthesis (3D-CoS), where 3D assets are constructed as executable Blender code, a programmatic and interpretable medium. To assess how well current VLMs can use code to represent 3D objects, we evaluate representative open-source and closed-source VLMs in code-based reconstruction under a unified protocol. We further introduce a suite ...

4. `2606.20112v1` score=0.3554
   Title: Pixel-Level Residual Diffusion Transformer: Scalable 3D CT Volume Generation
   Categories: cs.CV, eess.IV
   Abstract: Generating high-resolution 3D CT volumes with fine details remains challenging due to substantial computational demands and optimization difficulties inherent to existing generative models. In this paper, we propose the Pixel-Level Residual Diffusion Transformer (PRDiT), a scalable generative framework that synthesizes high-quality 3D medical volumes directly at voxel-level. PRDiT introduces a two-stage training architecture comprising 1) a local denoiser in the form of an MLP-based blind estimator operating on overlapping 3D patches to separate low-frequency structures efficiently, and 2) a global residual diffusion transformer employing memory-efficient attention to model and refine high-f...

5. `2606.11152v2` score=0.3468
   Title: P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning
   Categories: cs.CV
   Abstract: Multimodal large language models can write code to produce complex programs as well as use programs to do 3D modeling, which opens up a new avenue for 3D generation powered by their priors, world knowledge and reasoning. Yet existing benchmarks rarely evaluate 3D modeling through code. Such modeling demands more than runnable code: from a text or visual specification, a model must generate a parametric 3D program that is geometrically precise, semantically aligned and assembly-consistent. We introduce P3D-Bench, a benchmark for parametric 3D generation. Unlike a 3D mesh, a parametric 3D program exposes explicit dimensions, construction operations and part relations, revealing whether a model...

6. `2606.19776v1` score=0.3354
   Title: Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding
   Categories: cs.CV
   Abstract: Recently, vision-language models (VLMs) have made significant progress in 3D scene understanding, driving advances in applications such as embodied intelligence and robotic vision. However, existing approaches typically either rely directly on explicit 3D inputs (e.g., point clouds or RGB-D sequences), or introduce an additional 3D geometry encoder to derive 3D-aware visual tokens from 2D images. Such designs structurally decouple 3D geometric perception from the rich 2D semantics learned via vision-language pre-training, hindering the development of a unified 3D vision-language representation. In this work, we propose Occ-VLM, a novel framework for 3D scene understanding that operates purel...

7. `2606.10988v1` score=0.3343
   Title: AnimaSpark: A Feed-Forward Method for Animating Arbitrary 3D Objects
   Categories: cs.CV, cs.GR
   Abstract: While recent advancements in generative AI have substantially accelerated static 3D model creation workflows, the synthesis of category-agnostic 3D animations remains a significant bottleneck in 3D asset production. Current methods for category-agnostic animation generation exhibit critical limitations in inference speed, motion quality, and adherence to textual prompts, thereby leaving the process dependent on labor-intensive manual artistry. To address these challenges, this paper introduces AnimaSpark, a novel pipeline for category-agnostic 3D animation generation. Our approach is motivated by the key insight that for many fundamental motions in the 3D world, the corresponding joint trans...

8. `2606.08957v1` score=0.3314
   Title: Rethinking 3D Shape Generation: Diffusion over Superquadrics
   Categories: cs.CV
   Abstract: Diffusion models have advanced 3D shape generation, yet most methods still denoise in high-cardinality spaces (e.g., voxel/SDF grids, meshes, or point clouds), which is computationally and memory intensive and makes it difficult to scale in terms of both higher resolution and stronger controllability. We rethink the diffusion representation and propose to move diffusion from dense geometry to compact geometric primitives, representing each shape as a small set of superquadrics. Instead of operating on thousands to millions of geometric representation values, we leverage 7KB superquadric parameters (pose, size, and shape), drastically reducing diffusion-state dimensionality and per-step compu...


## Candidate 008

Query: text to 3D generation with signed distance fields

Likely paper IDs:

1. `2606.11152v2` score=0.2408
   Title: P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning
   Categories: cs.CV
   Abstract: Multimodal large language models can write code to produce complex programs as well as use programs to do 3D modeling, which opens up a new avenue for 3D generation powered by their priors, world knowledge and reasoning. Yet existing benchmarks rarely evaluate 3D modeling through code. Such modeling demands more than runnable code: from a text or visual specification, a model must generate a parametric 3D program that is geometrically precise, semantically aligned and assembly-consistent. We introduce P3D-Bench, a benchmark for parametric 3D generation. Unlike a 3D mesh, a parametric 3D program exposes explicit dimensions, construction operations and part relations, revealing whether a model...

2. `2606.20563v1` score=0.2291
   Title: JanusMesh: Fast and Zero-Shot 3D Visual Illusion Generation via Cross-Space Denoising
   Categories: cs.CV
   Abstract: Creating 3D visual illusions, a single 3D mesh that reveals entirely different semantics from various viewing angles, is a fascinating but tough challenge. Existing optimization-based methods are slow and can produce oversaturated colors. In contrast, naive stitching approaches fail to produce geometrically coherent objects. This results in visible unnatural seams and semantic leaks. In this paper, we present a fast and training-free framework for generating text-driven 3D visual illusions. Our approach decouples the generation into two stages. First, we propose a cross-space dual-branch denoising process. This process dynamically decodes 3D latents into voxel space for CLIP-guided orientati...

3. `2606.10478v1` score=0.2189
   Title: 3D-CoS: A New 3D Reconstruction Paradigm Based on VLM Code Synthesis
   Categories: cs.CV
   Abstract: Most recent 3D reconstruction and editing systems operate on implicit and explicit representations such as NeRF, point clouds, or meshes. While these representations enable high-fidelity rendering, they are fundamentally low-level and hard to control programmatically. In contrast, we propose and systematically evaluate a new 3D reconstruction paradigm, 3D Code Synthesis (3D-CoS), where 3D assets are constructed as executable Blender code, a programmatic and interpretable medium. To assess how well current VLMs can use code to represent 3D objects, we evaluate representative open-source and closed-source VLMs in code-based reconstruction under a unified protocol. We further introduce a suite ...

4. `2606.13364v1` score=0.2015
   Title: VideoMDM: Towards 3D Human Motion Generation From 2D Supervision
   Categories: cs.LG, cs.CV
   Abstract: We introduce VideoMDM, a diffusion-based framework that trains 3D human motion priors directly from accurate 2D poses extracted from monocular videos, without any 3D ground truth. A pretrained 2D-to-3D lifter provides approximate 3D pose sequences that serve as a noisy teacher: these are diffused, denoised by the model in 3D, and supervised in 2D by reprojecting the prediction and comparing against accurate keypoints. We show that, under mild assumptions, a depth-weighted 2D reprojection loss is equivalent in expectation to direct 3D supervision, and we adapt standard 3D motion regularizers - velocity consistency and over-parameterized representation alignment - to this 2D setting. Unlike me...

5. `2606.11446v1` score=0.2003
   Title: 3D-CBM: A Framework for Concept-Based Interpretability in Generative 3D Modeling
   Categories: cs.CV, cs.GR
   Abstract: This research introduces a framework for incorporating Concept Bottleneck Models (CBMs) into 3D generative architectures to address the inherent 'semantic gap' in deep geometric learning. As deep models become central to 3D content creation, explainability shifts from a peripheral feature to a fundamental requirement for trust and accountability in safety-critical domains such as healthcare and manufacturing. CBMs provide an intrinsic interpretability solution by constraining latent representations to align with human-defined concepts, yet their application to unstructured 3D data remains largely unexplored. We design, implement, and validate a formal 3D-CBM architecture that maps raw geomet...

6. `2606.10988v1` score=0.1946
   Title: AnimaSpark: A Feed-Forward Method for Animating Arbitrary 3D Objects
   Categories: cs.CV, cs.GR
   Abstract: While recent advancements in generative AI have substantially accelerated static 3D model creation workflows, the synthesis of category-agnostic 3D animations remains a significant bottleneck in 3D asset production. Current methods for category-agnostic animation generation exhibit critical limitations in inference speed, motion quality, and adherence to textual prompts, thereby leaving the process dependent on labor-intensive manual artistry. To address these challenges, this paper introduces AnimaSpark, a novel pipeline for category-agnostic 3D animation generation. Our approach is motivated by the key insight that for many fundamental motions in the 3D world, the corresponding joint trans...

7. `2606.20131v1` score=0.1933
   Title: TriFlow: Generating Artist-Like 3D Mesh Topology via Nearest-Vertex Vector Fields
   Categories: cs.CV, cs.GR
   Abstract: We present TriFlow, a new generative approach for producing compact 3D meshes with artist-like triangle topology directly from input geometry conditions such as signed distance fields. Our key insight is to represent mesh topology as a nearest-vertex vector field (NVF) defined over the surface, where each point encodes its association to the nearest triangle vertex in the local barycentric frame. We train a latent flow-matching model to synthesize this field, enabling topology generation conditioned on the input geometry. To extract a coherent mesh, we cluster surface regions using the generated NVF and guide a constrained quadric error metric (QEM) mesh simplification with topology-aware op...

8. `2606.19776v1` score=0.1874
   Title: Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding
   Categories: cs.CV
   Abstract: Recently, vision-language models (VLMs) have made significant progress in 3D scene understanding, driving advances in applications such as embodied intelligence and robotic vision. However, existing approaches typically either rely directly on explicit 3D inputs (e.g., point clouds or RGB-D sequences), or introduce an additional 3D geometry encoder to derive 3D-aware visual tokens from 2D images. Such designs structurally decouple 3D geometric perception from the rich 2D semantics learned via vision-language pre-training, hindering the development of a unified 3D vision-language representation. In this work, we propose Occ-VLM, a novel framework for 3D scene understanding that operates purel...


## Candidate 009

Query: robot learning with reinforcement learning and imitation learning

Likely paper IDs:

1. `2606.19752v1` score=0.3881
   Title: Temporal Self-Imitation Learning
   Categories: cs.RO, cs.AI
   Abstract: Long-horizon robot manipulation policies trained with reward shaping can still exploit dense rewards through inefficient interaction, while rare efficient behaviors may be forgotten during training. We argue that temporal efficiency itself provides a powerful and underutilized source of self-supervision for reinforcement learning. We introduce Temporal Self-Imitation Learning (TSIL), a reinforcement learning framework that mines temporally efficient successful trajectories generated during learning and converts them into reusable supervision for future policy improvement. TSIL progressively refines learning using configuration-conditioned adaptive temporal targets derived from fast successfu...

2. `2606.09758v1` score=0.3709
   Title: Difference-Aware Retrieval Policies for Imitation Learning
   Categories: cs.RO, cs.AI, cs.LG
   Abstract: Parametric imitation learning via behavior cloning can suffer from poor generalization to out-of-distribution states due to compounding errors during deployment. We show that reusing the training data during inference via a semi-parametric retrieval-based imitation learning approach can alleviate this challenge. We present Difference-Aware Retrieval Policies for Imitation Learning (DARP), a semi-parametric retrieval-based imitation learning approach that addresses this limitation by reparameterizing the imitation learning problem in terms of local neighborhood structure rather than direct state-to-action mappings. Instead of learning a global policy, DARP trains a model to predict actions ba...

3. `2606.15514v1` score=0.3635
   Title: Reinforcement Learning-Guided Retrieval with Soft Fusion for Robust Multimodal Imitation Learning under Missing Modalities
   Categories: cs.RO, cs.LG
   Abstract: Robotic systems perceive the world through multiple input modalities -- including visual camera streams and natural language instructions -- and must select appropriate actions based on these signals. However, assuming the permanent availability of all input devices is unrealistic, as sensors may fail, become occluded, or drop out entirely during deployment. Robust handling of such missing-modality scenarios is therefore essential for real-world robot operation. This paper introduces RL4IL, a reinforcement learning guided method for imitation learning that selects the most suitable action for a given observation by identifying the most relevant expert demonstrations from a training library. ...

4. `2606.16447v1` score=0.2772
   Title: Training and Evaluating Diffusion Policies with Long Context Lengths
   Categories: cs.RO, cs.AI
   Abstract: Imitation learning has enabled highly-dexterous robotic manipulation from RGB observations. Policies trained with these methods, however, typically condition robot actions on only a short history of observations. These policies cannot solve tasks that require memory and can get stuck repeatedly executing the same failing motions. In this work, we first benchmark policy performance as context length is incrementally increased from short to long, across a spectrum of tasks with varying local stability and memory requirements, and in multiple data regimes. To our knowledge, this is the first study to investigate context length in imitation learning at this level of detail. Our results challenge...

5. `2606.09499v1` score=0.2578
   Title: Targeting World Models to Compromise Robot Learning Pipelines
   Categories: cs.RO, cs.AI, cs.CR
   Abstract: World models have recently seen a rapid growth in both their popularity and capability as more data efficient tools for generating robot training data or simulating real world environments, with many works proposing their integration into the robot learning pipeline. While highly practical, in this work we demonstrate that world models introduce a uniquely stealthy and effective data poisoning entry point into the robot learning supply chain that can result in the deployment of unsafe or otherwise compromised robotic policies despite training on seemingly safe ground truth training data. In contrast to traditional data poisoning techniques which directly implant dangerous trajectories into s...

6. `2606.10613v1` score=0.2310
   Title: Fast and Highly Expressive Policy Learning for Offline Reinforcement Learning via Bootstrapped Flow Q-Learning
   Categories: cs.LG, cs.AI
   Abstract: Diffusion-based Q-learning has emerged as a powerful paradigm for offline reinforcement learning, but its reliance on multi-step denoising makes both training and inference computationally expensive and brittle. Recent efforts to accelerate diffusion Q-learning toward single-step action generation typically introduce auxiliary networks, policy distillation, or multi-phase training, which frequently compromise simplicity, stability, or performance. To address these limitations, we introduce Bootstrapped Flow Q-Learning (BFQ), a novel framework that enables accurate single-step action generation during both training and inference, without auxiliary networks or distillation procedures. BFQ adop...

7. `2606.11087v1` score=0.2302
   Title: Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning
   Categories: cs.LG, cs.AI
   Abstract: Expressive continuous control policies, such as diffusion and flow models, form the backbone of recent advances in scaling imitation learning for simulated and real robot control. While they are known to scale stably in the supervised imitation learning setting, incorporating them into reinforcement learning (RL) pipelines for policy improvement has proven more difficult. It often requires specialized training objectives or backpropagating through denoising processes, which cause well-known issues with stability and affect scalability. In this paper we study the question of whether simple policy improvement schemes at test time alone, leaving stable supervised policy training intact, can be ...

8. `2606.10170v1` score=0.2291
   Title: Learning Entropy and Spatial Adaptation Dynamics of Multilayer Perceptrons for Structural Point Extraction
   Categories: cs.LG
   Abstract: This paper extends the concept of Learning Entropy (LE) from temporal adaptive systems to spatial learning in multilayer perceptron networks (MLPs) applied to image data. Instead of evaluating image structure directly from gradients or covariance operators, as local neighborhood methods do, the proposed approach analyzes the learning process itself through Learning Entropy. An MLP is trained to predict the intensity of a center pixel from its surrounding spatial context, while LE is evaluated from the incremental adaptation of neural weights during learning across image-derived samples. The resulting Spatial Learning Entropy Maps (SLEM) identify unusual image points and regions that induce s...


## Candidate 010

Query: vision language models for robotics control

Likely paper IDs:

1. `2606.19584v1` score=0.2303
   Title: Language-Instructed Vision Embeddings for Controllable and Generalizable Perception
   Categories: cs.CV
   Abstract: Vision foundation models are typically trained as static feature extractors, placing the burden of task adaptation onto large downstream models. We propose an alternative paradigm: instead of solely feeding visual features into language models, we use language itself to dynamically guide the vision encoder. Our method, Language-Instructed Vision Embeddings (LIVE), leverages language as high-level guidance to produce task-centric embeddings at inference time, removing the need for task-specific retraining. This enables the encoder to focus on contextually relevant aspects of the input, yielding more controllable and generalizable representations. Empirically, LIVE reduces visual hallucination...

2. `2606.10918v1` score=0.2298
   Title: Task Robustness via Re-Labelling Vision-Action Robot Data
   Categories: cs.RO, cs.LG
   Abstract: The recent trend in scaling models for robot learning has resulted in impressive policies that can perform various manipulation tasks and generalize to novel scenarios. However, these policies continue to struggle with following instructions, likely due to the limited linguistic and action sequence diversity in existing robotics datasets. This paper introduces Task Robustness via Re-Labelling Vision-Action Robot Data (TREAD), a scalable framework that leverages large Vision-Language Models (VLMs) to augment existing robotics datasets without additional data collection, harnessing the transferable knowledge embedded in these models. Our approach leverages a pretrained VLM through three stages...

3. `2606.20272v1` score=0.2290
   Title: Efficiently Linking Real Scenes with Synthetic Data Generation for AI-based Cognitive Robotics and Computer Vision Applications
   Categories: cs.RO, cs.CV
   Abstract: AI vision models are a driving factor for the potential use case scenarios of cognitive robotics within in the industry and household applications. A large array of methods from semantic environment analysis towards 6D and grasping pose estimation have been proposed based on the latest AI achievements. However, such advancements require further strong and efficient methods w.r.t. training data and AI-architectures, which are capable in synergy to tackle current challenges, precision limits, and scalability beyond domain gaps. In this paper, we discuss these current limits and trends in the related state-of-the-art which are challenging those. Further we discuss our current work in progress o...

4. `2606.11563v1` score=0.2202
   Title: Cross-Modal Benchmarking for Robotic Perception in Natural Environments
   Categories: cs.CV, cs.RO
   Abstract: Natural environments present a complex challenge to robotics perception systems. Current models, particularly vision foundation models, are largely trained on structured, urban environments leading to weaknesses in their perception for field robotics tasks. We showcase the limitations of current models using our recently released WildCross benchmark, a new cross-modal benchmark for place recognition and metric depth estimation in large-scale natural environments. WildCross comprises over 476K sequential RGB frames with semi-dense depth and surface normal annotations, each aligned with accurate 6DoF pose and synchronized dense lidar submaps. In this work, we provide an expanded analysis of th...

5. `2606.12365v1` score=0.2128
   Title: Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics
   Categories: cs.RO, cs.AI
   Abstract: We propose Ambient Diffusion Policy, a simple and principled method for imitation learning from suboptimal data in robotics. High-quality, task-specific robot data is expensive and time-consuming to collect, while suboptimal datasets with lower-quality or out-of-distribution demonstrations are abundant. Existing methods that co-train on both data sources in robotics often fail to separate the meaningful and the harmful features in the suboptimal samples. In contrast, our method extracts only the useful features by introducing a new axis to co-training in robotics: noise-dependent data usage. Ambient Diffusion Policy restricts the contribution of suboptimal data during training to only the hi...

6. `2606.11906v1` score=0.2060
   Title: When Does Language Matter? Multilingual Instructions Reveal Step-wise Language Sensitivity in Vision-Language-Action Models
   Categories: cs.CL
   Abstract: Vision-Language-Action (VLA) models have shown strong performance in language-conditioned robotic manipulation, yet their robustness to linguistic variation remains poorly understood. In this work, we present the first systematic multilingual evaluation of VLA models by translating the LIBERO benchmark into ten languages, revealing severe performance degradation under non-English instructions, with success rates dropping by 30-50%. Through fine-grained analysis of task executions, we find that language influence is highly non-uniform across steps: certain steps exhibit strong language dependence and dominate overall task failure, while others are largely language-agnostic. Based on this insi...

7. `2606.09009v1` score=0.1992
   Title: Scaling by Diversified Experience for Vision-Language-Action Models
   Categories: cs.CV
   Abstract: Vision-Language-Action models face significant challenges in real-world deployment due to the entanglement of high-level reasoning with low-level control, and the instability of policy optimization. In this paper, we introduce SyVLA, a robust VLA model trained with diversified experiences. We propose an Intention Decoupling algorithm to isolate control-relevant features from reasoning contexts and a similar-sample guided RL pipeline to stabilize policy updates and mitigate distribution shift. Extensive experiments on real-world robotic tasks and multi-modal benchmarks demonstrate that SyVLA achieves superior task success rates and stronger out-of-distribution generalization compared to exist...

8. `2606.08775v1` score=0.1936
   Title: Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks
   Categories: cs.RO, cs.AI
   Abstract: Visual world models have shown great potential in learning complex system dynamics. Recent advancements leverage these models as transition functions within Model Predictive Control (MPC) frameworks to solve various control tasks. When applied to robotics, however, they are limited to single-stage tasks such as reaching or grasping, and struggle with multi-stage ones that demand complex sequential planning. In this work, we introduce WorldDP, a world model framework designed for multi-stage robotic manipulation. Our hierarchical approach utilizes a high-level world model as a transition function to optimize for feasible subgoals during runtime, which are subsequently reached by a low-level D...


## Candidate 011

Query: privacy preserving machine learning with differential privacy

Likely paper IDs:

1. `2606.09582v1` score=0.5121
   Title: On Choosing the $μ$ Parameter in Gaussian Differential Privacy
   Categories: cs.LG, stat.ML
   Abstract: Recent work argues for using Gaussian differential privacy (GDP) to report the privacy guarantees in privacy-preserving machine learning. We provide principled mappings from pure-DP $\varepsilon$ to GDP $μ$ by matching the worst-case success of a strong-adversary membership inference attack in terms of three metrics: multiplicative advantage at fixed FPR, precision at fixed recall, and the standard privacy profile. We tabulate $μ$ values across a useful range of parameters and recommend $μ\approx \varepsilon/5$ as a conservative general-purpose conversion.

2. `2606.07175v1` score=0.4668
   Title: Seeing Without Exposing: Adaptive Privacy Control for Open-World, Context-Hungry MLLMs
   Categories: cs.CV
   Abstract: Multimodal large language models (MLLMs) have raised new privacy challenges. On the data side, user-provided inputs often include unpredictable sensitive information; while on the downstream task side, model reasoning depends on rich visual context that may itself be privacy-sensitive. Existing privacy protection methods, however, rely on predefined sensitive categories and fixed obfuscation strategies, struggling to tackle such challenges in MLLMs. To address this dilemma, we propose Anchored Privacy Drifting (APD), a training-free method that drifts privacy-sensitive elements toward semantically equivalent alternatives while anchoring contextual cues to the source image. To systematically ...

3. `2606.09132v1` score=0.4617
   Title: Vision Language Model Helps Private Information De-Identification in Vision Data
   Categories: cs.AI
   Abstract: Visual Language Models (VLMs) have gained significant popularity due to their remarkable ability. While various methods exist to enhance privacy in text-based applications, privacy risks associated with visual inputs remain largely overlooked such as Protected Health Information (PHI) in medical images. To tackle this problem, two key tasks: accurately localizing sensitive text and processing it to ensure privacy protection should be performed. To address this issue, we introduce VisShield (Vision Privacy Shield), an end-to-end framework designed to enhance the privacy awareness of VLMs. Our framework consists of two key components: a specialized instruction-tuning dataset OPTIC (Optical Pri...

4. `2606.09401v1` score=0.4609
   Title: Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models
   Categories: cs.LG, cs.CR
   Abstract: Recent work has applied differential privacy (DP) to adapt large language models (LLMs) for sensitive applications, offering theoretical guarantees. However, its practical effectiveness remains unclear, partly due to LLM pretraining, where overlaps and interdependencies with adaptation data can undermine privacy despite DP efforts. To analyze this issue in practice, we investigate privacy risks under DP adaptations in LLMs using state-of-the-art attacks such as robust membership inference and canary data extraction. We benchmark these risks by systematically varying the adaptation data distribution, from exact overlaps with pretraining data, through in-distribution (IID) cases, to entirely o...

5. `2606.09125v1` score=0.4206
   Title: Unveiling Privacy Risks in Multi-modal Large Language Models: Task-specific Vulnerabilities and Mitigation Challenges
   Categories: cs.CR, cs.AI
   Abstract: Privacy risks in text-only Large Language Models (LLMs) are well studied, particularly their tendency to memorize and leak sensitive information. However, Multi-modal Large Language Models (MLLMs), which process both text and images, introduce unique privacy challenges that remain underexplored. Compared to text-only models, MLLMs can extract and expose sensitive information embedded in images, posing new privacy risks. We reveal that some MLLMs are susceptible to privacy breaches, leaking sensitive data embedded in images or stored in memory. Specifically, in this paper, we (1) introduce MM-Privacy, a comprehensive dataset designed to assess privacy risks across various multi-modal tasks an...

6. `2606.16801v1` score=0.3695
   Title: The Art of Mixology: Mixup-based Obfuscation for Privacy-Preserving Split Learning in Large Language Models
   Categories: cs.CL
   Abstract: Split learning provides a practical paradigm for resource-constrained users to train Large Language Models (LLMs) by offloading computation-intensive layers to a server while keeping raw data local. However, existing privacy-preserving split learning methods still face a difficult trade-off among utility, privacy, efficiency, and stability. Specifically, these methods often suffer from substantial utility degradation, remain vulnerable to advanced data reconstruction attacks, incur prohibitive computational and communication overhead, or exhibit unstable performance across different tasks. In this paper, we propose MIXGUARD, a novel mixup-based privacy-preserving split learning framework for...

7. `2606.10173v1` score=0.3513
   Title: Local Is Not a Sufficient Privacy Boundary: Governing OS-Integrated On-Device AI
   Categories: cs.CR, cs.AI
   Abstract: As AI systems move into operating systems, privacy no longer turns only on whether a model runs locally. A local assistant may assemble email, calendar entries, files, screenshots, notifications, and app intents; retain embeddings or summaries; invoke tools; emit telemetry; or route difficult requests to cloud infrastructure. Local inference reduces some exposure, but it answers only one question: where computation occurs. It does not answer who may assemble context, what derived state persists, which actions are authorized, or how updates change the system's authority. We develop an OS-centered privacy framework for on-device AI that treats privacy as an institutional accountability problem...

8. `2606.10481v1` score=0.3419
   Title: Advancing the State-of-the-Art in Empirical Privacy Auditing
   Categories: cs.LG, cs.AI, cs.CL, cs.CR, stat.ML
   Abstract: Parameter-efficient fine-tuning of large language models (LLMs) can exhibit problematic memorization of individual training examples. Empirical privacy auditing (EPA) quantifies this risk by measuring realistic data leakage on membership inference (MI) or reconstruction attacks. A key challenge in EPA is designing ``canary'' examples that are mixed with the privacy-sensitive training data. We propose generating synthetic canaries via high-temperature sampling ($T \geq 0.8$) from LLMs, using prompts tailored to the privacy-sensitive training data. These canaries act as high-influence outliers, ensuring high identifiability and hence strong audits. Further, since the canaries are themselves no...


## Candidate 012

Query: model watermarking and provenance for generative AI

Likely paper IDs:

1. `2606.10937v1` score=0.3494
   Title: Provenance Tracking in AI Compilers through the Lens of Coalgebra
   Categories: cs.DB, cs.AI
   Abstract: AI compilers aggressively rewrite computation graphs through normalization, lowering, and optimization, making it difficult to track the provenance of tensors and operators across compilation. Reliable provenance is essential for attaching platform-specific postprocessing, debugging compiler behavior, and validating transformations, yet existing solutions are either invasive or ad hoc under non-injective graph rewrites. We present a lightweight, generative approach to provenance tracking based on observational semantics. Instead of propagating identifiers through compiler passes, we observe graph transformations and reason about provenance in terms of observable computational actions. We for...

2. `2606.17123v1` score=0.3047
   Title: LineageMark: Multi-user White-box Watermarking for Contribution Tracing in Model Derivation Chains
   Categories: cs.CR, cs.AI
   Abstract: In open large language model (LLM) ecosystems, models are frequently adapted across multiple domains and applications, forming multi-stage derivation chains. Consequently, tracking and verifying historical contributions is essential for model provenance and intellectual property protection. However, existing watermarking methods are mainly designed for single-user, one-time embeddings, often fail under repeated model derivation and incremental updates. To address this problem, we propose LineageMark, a multi-user white-box watermarking framework for model derivation chains. The framework encodes watermarks in model parameters using a projection-based approach. Stable carriers are first selec...

3. `2606.11828v1` score=0.2296
   Title: Feature-Aligned Speech Watermarking for Robustness to Reconstruction Distortions
   Categories: cs.SD, cs.AI, cs.CR, cs.MM
   Abstract: Audio watermarking aims to embed identifiable information into audio while remaining imperceptible. Existing methods adopt high-fidelity, low-energy designs to preserve perceptual quality, but the resulting watermarks lack robustness under suppression by speech reconstruction models. Improving robustness is challenging due to the inherent robustness-fidelity trade-off in existing designs, where increasing watermark energy improves robustness but reduces fidelity. To address this problem, we propose a feature-aligned watermarking method that aligns the watermark with the original speech feature distribution, allowing higher watermark energy to improve robustness while preserving imperceptibil...

4. `2606.11698v1` score=0.1985
   Title: T2S: A Rehearsal-Based Approach for Extraction-Resistant Model Watermarking
   Categories: cs.CR, cs.AI
   Abstract: Model watermarking safeguards AI model intellectual property by embedding distinctive knowledge that induces unique behavioral signatures. The primary technical challenge lies in ensuring watermark robustness against various post-processing attacks on the watermarked model. Model extraction attacks emerge as the most severe threat, where adversaries exploit prediction outputs to train surrogate models that illegally replicate the original model's functionality. In this work, we propose a rehearsal-based watermark embedding framework to enhance the robustness of model watermarks against model extraction attacks. By simulating the extraction process, our method leverages the loss of a \textit{...

5. `2606.15246v1` score=0.1897
   Title: Provenance-Enhanced Statements in Knowledge Graphs
   Categories: cs.LO, cs.AI, cs.DL
   Abstract: Provenance-enhanced statements of the form "according to $X$, $\varphi$" are pervasive in contemporary knowledge graphs, especially in domains where graph content primarily represents claims, interpretations, and hypotheses (\emph{capta}) rather than observer-independent facts (\emph{data}). Current provenance models can record who asserted what, but they typically treat provenance as semantically neutral, leaving underspecified how attributed claims relate to factual commitment, to one another, and to reasoning. In this paper we introduce DEC, a framework that interprets provenance predicates as indicators of epistemic stance and groups provenance-homogeneous sets of statements into \emph{c...

6. `2606.10612v1` score=0.1803
   Title: GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning
   Categories: cs.CV
   Abstract: 3D Gaussian Splatting (3DGS) is a powerful technique for creating high-fidelity 3D assets. However, the widespread sharing and iterative modification of 3DGS models across digital platforms create pressing challenges for intellectual property protection and forensic traceability. To address this, we propose GaussTrace, a novel framework for constructing directed provenance graphs for 3DGS models. GaussTrace formulates provenance analysis as an evidence-based reasoning problem. It builds upon attribute-wise statistical profiling of 3DGS parameters to capture intrinsic properties. Moreover, we introduce hypothesis-driven editing simulations of common operations to provide auxiliary evidence fo...

7. `2606.15833v1` score=0.1723
   Title: When Correct Edges Cannot Be Verified: A Provenance Gap in Incomplete KGQA and a Provenance-Favoring Completion Policy
   Categories: cs.CL
   Abstract: Incomplete Knowledge Graph Question Answering (IKGQA) requires completing missing edges to continue reasoning. A growing line of work verifies completed edges against retrieved text, treating textual support as a proxy for edge quality. We ask a question that, to our knowledge, has not been systematically tested: does textual verifiability actually track correctness? Exploiting the gold deleted triples provided by the standard random-deletion protocol, we measure both. The finding is counterintuitive: among gold-correct completed edges, 76-96% have no supporting passage even under exhaustive retrieval, robustly across deletion rates (20%/40%), datasets (CWQ/WebQSP), and relation types (struc...

8. `2606.19753v1` score=0.1537
   Title: Grounded Inference: Principles for Deterministically Encapsulated Generative Models
   Categories: cs.AI, cs.SE
   Abstract: The incorporation of generative models into traditional computational systems presents both enormous opportunity and tremendous peril. Although many early adopters have realized these perils at great expense, the field still requires foundational frameworks to de-risk incorporation of AI into traditional systems. This manuscript establishes this foundation through the definition of four specific primitives of AI blended architecture, designed to enable deterministic encapsulation of probabilistic models. It further establishes two overarching anti-patterns broadly represented across industry to serve as warnings for engineers in this field. This framework was designed to enable successful in...


## Candidate 013

Query: efficient fine tuning of large language models

Likely paper IDs:

1. `2606.14970v1` score=0.3818
   Title: Zero-order Parameter-free Optimization for LMO-based Methods: Novel Approach for Efficient Fine-tuning
   Categories: cs.LG
   Abstract: Fine-tuning large language models (LLMs) has become a central application of modern optimization, enabling pretrained models to adapt to diverse downstream tasks and domain-specific data. A major obstacle in large-scale fine-tuning is the memory overhead of backpropagation, which requires storing activations, gradients, and optimizer states. Zeroth-order (ZO) optimization offers a memory-efficient alternative, but its performance is highly sensitive to the stepsize and smoothing parameter, often requiring costly task-specific tuning. Parameter-free (PF) optimization addresses this issue by adapting algorithmic parameters without prior knowledge of problem-dependent constants. Moreover, large...

2. `2606.11854v1` score=0.3539
   Title: Fine-tuning Multi-modal LLMs with ART: Art-based Reinforcement Training
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: There are two main Parameter-Efficient Fine-Tuning (PEFT) techniques for Large Language Models (LLMs). While Low-Rank Adaptation (LoRA) introduces additional weights between the LLM layers, Soft Prompting introduces additional fine-tuning-specific raw tokens to an LLM input. However, both require modification to the computational graphs of precompiled, preoptimized LLMs. As a result, neither is fully supported in high-throughput engines like vLLM. We propose fine-tuning with ART (Art-based Reinforcement Training). The method injects information into a frozen Multimodal Large Language Model (MLLM) by optimizing only its raw visual input, thus enabling the soft-token approach on pre-compiled c...

3. `2606.08994v1` score=0.3040
   Title: Language-Aware Token Boosting: LLM Language Confusion Reduction Without Tuning
   Categories: cs.CL
   Abstract: Large language models (LLMs) sometimes exhibit language confusion when generating non-English text. Existing approaches typically rely on fine-tuning to mitigate this issue. In contrast, we propose a tuning-free paradigm for reducing language confusion. Within this paradigm, we introduce two methods: Language-Aware Token Boosting (LATB), which applies targeted perturbations to tokens associated with the desired language, and Adaptive Language-Aware Token Boosting (Adaptive-LATB), which dynamically adjusts these perturbations based on the model's confidence in the intended language. Experiments demonstrate that our methods effectively improve multilingual alignment by reducing language confus...

4. `2606.19528v1` score=0.2839
   Title: Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge Devices
   Categories: cs.LG, cs.AI
   Abstract: Fine-tuning of Large Language Models (LLMs) using Low-Rank Adaptation (LoRA) on an end-user's data offers personalized experiences while keeping data private, but faces severe memory constraints on consumer hardware. Peak memory during fine-tuning often exceeds device limits, especially for models with billions of parameters and long-context training data. This paper introduces a suite of complementary techniques to reduce memory footprint without sacrificing model quality: (1) base model quantization with on-the-fly dequantization, (2) memory-efficient checkpointing combining selective activation caching and disk offloading, (3) softmax approximation using semantically relevant token subset...

5. `2606.09068v1` score=0.2793
   Title: Emergent Misalignment Can Be Induced by Sycophancy and Reversed via Alignment Gating
   Categories: cs.CL
   Abstract: Prior work has shown that fine-tuning large language models on malicious or incorrect outputs in narrow domains can induce broad misalignment and harmful behavior, a phenomenon known as emergent misalignment. However, efficient methods for reversing such misalignment remain limited. In this work, we make two contributions. First, we identify sycophancy fine-tuning, i.e., training models to passively agree with users' incorrect opinions, as a previously underexplored driver of emergent misalignment, and show that it induces broad and severe misaligned behavior. Second, we propose Alignment Gating, an efficient method for reversing emergent misalignment that inserts learnable and controllable ...

6. `2606.17660v1` score=0.2718
   Title: TuneAhead: Predicting Fine-tuning Performance Before Full Training Begins
   Categories: cs.LG, cs.AI
   Abstract: Fine-tuning large language models (LLMs) is compute-intensive and error-prone: model performance depends sensitively on data quality and hyperparameter choices, and naïve runs can even degrade model performance. This raises a practical question:can we predict fine-tuning performance before committing to a full training run? We present TUNEAHEAD, a lightweight framework for pre-hoc prediction of fine-tuning performance. TUNEAHEAD encodes each candidate run as a meta-feature vector that combines static dataset descriptors with dynamic probe features from a short standardized probe. A predictor maps these features to performance estimates, while SHAP-based attributions provide interpretable dia...

7. `2606.17820v1` score=0.2617
   Title: Improving low-resource ASR using bilingual fine-tuning with language identification: a cross-linguistic evaluation
   Categories: cs.CL
   Abstract: This study explores how bilingual fine-tuning affects automatic speech recognition (ASR) in low-resource languages. We evaluate this method across nine linguistically and geographically diverse language pairs, covering a range of language families and writing systems. To distinguish the two languages, during training, we pre-pend each input text with a language identification token. At inference, the model jointly predicts both the language and transcription from the speech input alone. As texts for which the language is incorrectly determined show low ASR performance, we also conduct a follow-up experiment in which the language identification token is provided both during training and infer...

8. `2606.18472v1` score=0.2410
   Title: Domain Generalizable Adaptation of 3D Vision-Language Models via Regularized Fine-Tuning
   Categories: cs.CV
   Abstract: Domain adaptation remains a central challenge in 3D vision, especially for multimodal foundation models that align 3D point clouds with visual and textual data. While these models demonstrate strong general capabilities, adapting them to downstream domains with limited data often leads to overfitting and catastrophic forgetting. To address this, we introduce ReFine3D, a regularized fine-tuning framework designed for domain-generalizable tuning of 3D large multimodal models (LMMs). ReFine3D combines selective layer tuning with two targeted regularization strategies: multi-view consistency across augmented point clouds and text diversity through synonym-based prompts generated by large languag...


## Candidate 014

Query: parameter efficient adaptation for multimodal models

Likely paper IDs:

1. `2606.10196v1` score=0.2356
   Title: Fisher-Guided Progressive Parameter Selection for Adaptive Fine-Tuning
   Categories: cs.CV, cs.AI
   Abstract: Parameter-efficient fine-tuning (PEFT) aims to adapt pretrained models with a small trainable parameter subset, however, most existing methods choose this subset from fixed architectural heuristics rather than using dynamic, task-aware criteria. We introduce \textbf{FisherAdapTune}, a Fisher-guided Adaptive Fine-Tuning framework that progressively selects parameter groups by tracking the temporal drift of their Fisher geometry. Starting from a PAC-Bayesian view of fine-tuning, we decompose the generalization error bound into Fisher-weighted update costs and show that parameter groups whose curvature contribution has stabilized can be frozen to reduce the error bound without interrupting the ...

2. `2606.14222v1` score=0.2336
   Title: Learning the Context of Errors: Black-Box Online Adaptation of Time Series Foundation Models
   Categories: cs.LG
   Abstract: The rapid evolution of Time Series Foundation Models (TSFMs) has advanced zero-shot forecasting across diverse domains. Inspired by the current form of Large Language Models, future TSFMs may be offered as commercialized, closed-source API services. However, many existing online adaptation methods still rely on white-box access for parameter fine-tuning or gradient backpropagation. This paradigm mismatch raises a question: In black-box online adaptation for TSFMs, what should we learn? We answer this with an insight: the predictive errors of the base model are conditioned on both the input and output of the base model (i.e., the context of errors). To validate this insight, we propose ORCA (...

3. `2606.09148v1` score=0.2236
   Title: Explicit Representation Alignment for Multimodal Sentiment Analysis
   Categories: cs.CL
   Abstract: Multimodal affective analysis aims to understand human sentiment and emotion by jointly modeling heterogeneous modalities such as text and images. However, multimodal models often fail to consistently outperform strong text-only baselines, with performance varying significantly across fusion strategies. In this work, we identify representation misalignment between independently pretrained modality encoders as a key bottleneck for effective multimodal learning, and show through controlled experiments that alignment prior to fusion is often more important than fusion complexity. To address this issue, we propose a unified multimodal affective analysis framework that leverages vision-language m...

4. `2606.13767v1` score=0.2131
   Title: Beyond LoRA: Is Sparsity-Induced Adaptation Better?
   Categories: cs.LG, cs.AI, cs.IT
   Abstract: Low-rank adaptation (LoRA) and its variants provide a memory- and compute-efficient alternative to full fine-tuning of pre-trained models. However, questions remain about the comparative generalizability of these approaches and how the structural restrictions on low-rank updates preserve effective adaptation performance. We present a historical framing, covering the past (full fine-tuning and original LoRA), the present (different variants of LoRA), and propose simpler, cheaper, parameter-efficient extensions by inducing sparsity within existing LoRA variants: Cheap LoRA (cLA), training a single low-rank factor with the other fixed (deterministically or, in its randomized variant, stochastic...

5. `2606.14299v1` score=0.2109
   Title: What Drives Test-Time Adaptation for CLIP? A Controlled Empirical Study from an Update Perspective
   Categories: cs.CV, cs.LG
   Abstract: Vision-Language Models (VLMs) such as CLIP have become a standard backbone for open-vocabulary recognition, yet their zero-shot predictions remain vulnerable to distribution shifts encountered at deployment. Test-Time Adaptation (TTA) has recently been extended to CLIP as a lightweight solution, leading to a rapidly growing body of TTA4CLIP methods. However, empirical progress in this area has largely outpaced our understanding of what truly drives adaptation, where their gains originate, and under which shifts they remain reliable. In this paper, we take a step back from the pursuit of state-of-the-art accuracy and conduct a systematic controlled study of TTA4CLIP. We first organize existin...

6. `2606.17213v1` score=0.2044
   Title: Revisiting LLM Adaptation for 3D CT Report Generation: A Study of Scaling and Diagnostic Priors
   Categories: cs.CL, cs.CV
   Abstract: Recent advances in multimodal learning, including large language models (LLMs) and vision-language models (VLMs), have demonstrated strong adaptability to natural images. However, extending their use to the medical domain, particularly for volumetric (3D) images, is challenging due to high computational complexity, volumetric dependencies and the semantic gap between visual features and clinical terminology. Naively fine-tuning LLMs on limited medical data often leads to overfitting and clinical hallucination, where linguistic fluency is prioritized over clinical factuality. In this study, we investigate parameter-efficient adaptation strategies for volumetric CT report generation and introd...

7. `2606.09401v1` score=0.1932
   Title: Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models
   Categories: cs.LG, cs.CR
   Abstract: Recent work has applied differential privacy (DP) to adapt large language models (LLMs) for sensitive applications, offering theoretical guarantees. However, its practical effectiveness remains unclear, partly due to LLM pretraining, where overlaps and interdependencies with adaptation data can undermine privacy despite DP efforts. To analyze this issue in practice, we investigate privacy risks under DP adaptations in LLMs using state-of-the-art attacks such as robust membership inference and canary data extraction. We benchmark these risks by systematically varying the adaptation data distribution, from exact overlaps with pretraining data, through in-distribution (IID) cases, to entirely o...

8. `2606.19266v1` score=0.1922
   Title: Trade-offs in Medical LLM Adaptation: An Empirical Study in French QA
   Categories: cs.CL, cs.AI
   Abstract: The development of large language models (LLMs) has led to an increased focus on their adaptation to specialized domains and languages, yet the effectiveness of domain adaptation strategies remains unclear. We present a study of medical domain adaptation using French medical question-answering (QA) as a case study. We compare continual pretraining (CPT), supervised fine-tuning (SFT), and their combination across three model families, multiple sizes, and three initialization types, explicitly disentangling adaptation effects from base model choice. We evaluate both multiple-choice (MCQA) and open-ended QA (OEQA) under greedy and constrained decoding using automatic metrics and LLM-as-a-Judge ...


## Candidate 015

Query: long context language model retrieval and memory

Likely paper IDs:

1. `2606.10694v1` score=0.4212
   Title: REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs
   Categories: cs.CL
   Abstract: Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons. However, due to their finite context window, LLMs cannot retain all past interactions, making long-term memory management essential for storing, updating, and retrieving historical information beyond the context limit. Although recent memory systems attempt to address this issue by storing historical information externally, existing approaches suffer from three key limitations: flat text-based memory organizations fail to capture explicit relations among memories, structured memory systems often destructively overwrite evolving facts, and current retrieval mechanisms remain query-agnostic a...

2. `2606.13115v1` score=0.4131
   Title: G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents
   Categories: cs.CL, cs.AI
   Abstract: While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context reasoning and the inefficiency of processing extensive raw text. Existing approaches typically rely on either unstructured memory storage, which is prone to information loss, or computationally expensive LLMs that incur high latency. To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs. Furthermore, we introduce the novel attention-aware impo...

3. `2606.16449v2` score=0.4097
   Title: PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory
   Categories: cs.CV
   Abstract: Consistent video generation under editing operations requires persistence: when edits modify scene appearance or layout, subsequent generations should remain coherent across time and viewpoints. However, existing memory designs struggle to maintain long-term consistency after such modifications, as stored contexts may become outdated or invalid. To address this, we propose PermaVid, a novel framework built upon a multi-modal context memory that disentangles spatial context into semantic appearance and geometric structure, together with an edit-aware memory update and retrieval strategy that keeps memory evolution aligned with subsequent observations. Specifically, we develop two complementar...

4. `2606.14047v1` score=0.3702
   Title: Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling
   Categories: cs.IR, cs.AI, cs.CL, cs.LG
   Abstract: Long-context language modeling requires not only extending context windows but maintaining coherent understanding of entity states and relationships across thousands of tokens -- a challenge that semantic similarity alone cannot address. KGERMAR addresses this by constructing dynamic, context-specific knowledge graphs from input text during inference, enabling domain-adaptive retrieval that leverages both semantic similarity and explicit entity relationships. The framework performs real-time entity and relation extraction to build contextual knowledge graphs, then integrates graph-structural embeddings with textual semantics through a multi-component memory architecture. Three memory banks -...

5. `2606.10677v1` score=0.3489
   Title: Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory
   Categories: cs.AI, cs.CL
   Abstract: Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference tim...

6. `2606.07711v1` score=0.3063
   Title: Rosetta Memory: Adaptive Memory for Cross-LLM Agents
   Categories: cs.LG, cs.AI
   Abstract: Memory is the key component for transforming a stateless LLM into a persistent, evolving agent through experience accumulation, long-horizon planning, and continual self-improvement. Existing memory systems typically take the LLM as the center and design memory operations tailored to a specific backbone. In practice, however, users frequently switch between LLMs, for example using Claude for coding and GPT for writing across tasks, or routing different steps to different backbones within a single task for cost-effective trade-offs. As a result, memory written by one model often needs to be consumed by another. Making upstream memory effectively adapt to and activate downstream LLMs remains a...

7. `2606.10532v1` score=0.3043
   Title: ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning
   Categories: cs.AI
   Abstract: Memory is essential for enabling large language model (LLM) agents to handle long-horizon reasoning tasks. Existing memory mechanisms are largely centralized, typically organizing retrieved information and interaction history within a single model context. This design imposes a fundamental trade-off: scaling reasoning trajectories risks context overload, whereas aggressive content pruning may result in irreversible information loss. Seeking a better trade-off, we draw inspiration from human cognitive systems, especially the functional complementarity between the prefrontal cortex (executive control) and the hippocampus (memory management), suggesting that such a trade-off need not be inheren...

8. `2606.18829v1` score=0.3040
   Title: GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents
   Categories: cs.LG, cs.CL
   Abstract: Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. In these deployments, multiple principals write to a common memory pool and query it under different roles, scopes, and relationships, so memory quality requires governance as well as recall. We introduce GateMem, a benchmark for multi-principal shared-memory agents. GateMem jointly evaluates utility for legitimate long-horizon requests with state updates, access control across contextual authorization boundaries, and agent-facing active forgetting after explicit deletion requests. It spans medical, office, education, and household ...


## Candidate 016

Query: uncertainty estimation for large language models

Likely paper IDs:

1. `2606.11512v1` score=0.3838
   Title: SAGE: Answer-Conditioned Uncertainty Targets for Verbal Uncertainty Alignment
   Categories: cs.CL
   Abstract: Large language models increasingly express uncertainty through natural-language statements, yet these expressions often fail to reflect the model's sampled behavior. We study verbal uncertainty alignment as a distributional calibration problem: the appropriate uncertainty target for a prompt should be estimated from repeated model outputs rather than from an isolated response. However, group rollouts alone are insufficient, since the resulting target must provide a useful training signal. Existing targets only partially satisfy this requirement. We propose SAGE, Semantic-Answer Guided Entropy, a group-level uncertainty target that constructs an answer-conditioned uncertainty geometry over sa...

2. `2606.11870v1` score=0.3641
   Title: Modelling magnetic material properties with uncertainty-aware neural networks
   Categories: cond-mat.mtrl-sci, cs.LG
   Abstract: Machine learning is increasingly applied to accelerate the discovery of novel materials by exploring large compositional and structural design spaces. Yet, the scarcity of high-quality data and the frequent need for out-of-distribution prediction introduce substantial uncertainty, making the assessment of model reliability essential. In this work, we investigate uncertainty quantification as a means to evaluate model confidence in the context of permanent magnet research. In a first study, we benchmark classical and modern machine learning models for predicting intrinsic magnetic properties, focusing on the quality of their uncertainty estimates. We apply Gaussian negative log-likelihood los...

3. `2606.13451v1` score=0.2956
   Title: Uncertainty Estimation for Molecular Diffusion Models
   Categories: cs.LG
   Abstract: Diffusion models have seen wide adoption for 3D molecular generation, yet they offer no principled signal of when a generated molecule is likely to be of low quality. We propose a post-hoc method for estimating per-sample uncertainty in pretrained molecular diffusion models. Building on a Laplace approximation of the denoising network, we measure the variability of the noise prediction across the generation trajectory. Empirically, we show that the resulting uncertainty score is informative of sample quality, exhibiting a negative correlation with established sample-level quality metrics. We further study how the proposed uncertainty score can be used to filter generated samples, improving m...

4. `2606.15767v1` score=0.2838
   Title: Visualizing Uncertainty: Spatial Maps of Missing and Conflicting Evidence in Deep Learning
   Categories: cs.LG, cs.AI
   Abstract: Understanding when and why deep neural networks are uncertain is crucial for deploying reliable machine learning systems in safety-critical domains. While existing uncertainty quantification methods provide scalar measures of model confidence, they offer limited insight into which spatial regions of an input contribute to different types of uncertainty. We propose a novel visualization framework, Uncertainty Activation Map (UAM), that combines Evidential Deep Learning (EDL) with Full-Gradient Class Activation Mapping (FullGrad) to generate interpretable spatial uncertainty activation maps. Our approach distinguishes between two fundamental types of uncertainty: vacuity, representing lack of ...

5. `2606.09923v1` score=0.2788
   Title: Conformal Prediction for Neural Operators: Distribution-Free Uncertainty Quantification in Physics Simulation
   Categories: cs.LG, cs.AI
   Abstract: Neural operators such as the Fourier Neural Operator (FNO) have emerged as powerful surrogates for solving partial differential equations (PDEs), achieving speedups of several orders of magnitude over traditional numerical solvers. However, deploying these models in safety-critical engineering applications -- such as thermal management of electronic components and battery systems -- requires not only accurate point predictions but also rigorous uncertainty guarantees. Existing uncertainty quantification (UQ) methods for neural operators, including Monte Carlo Dropout and Deep Ensembles, provide only relative uncertainty estimates without formal coverage guarantees. In this work, we propose t...

6. `2606.11012v1` score=0.2656
   Title: An Uncertainty Estimation Framework for Dose Accumulation in Adaptive Radiotherapy: Application to CBCT-Guided Radiotherapy for Cervical Cancer
   Categories: cs.CV
   Abstract: Background and purpose: oART enables daily plan adaptation to interfraction anatomical variations, but cumulative dose estimation remains limited by DIR, segmentation, and anatomical uncertainties. We introduce IMPACT-DoseAcc, an uncertainty-aware dose accumulation framework, within IMPACT for semantic feature-driven image analysis. The framework is modality- and disease-agnostic and is applied to CBCT-guided oART for cervical cancer (LACC). Material and Methods: Nine LACC patients were retrospectively analyzed using daily CBCT-derived virtual CTs for dose recalculation. IMPACT-DoseAcc focuses on uncertainty from DIR, without modeling vCT-generation uncertainty. Two DIR uncertainty strategie...

7. `2606.18043v1` score=0.2645
   Title: Uncertainty Quantification for Flow-Based Vision-Language-Action Models
   Categories: cs.RO, cs.LG
   Abstract: Vision-language-action models (VLAs) combine vision-language backbones with expressive generative action heads trained via flow matching on large-scale robotic datasets. Despite their strong empirical performance in robotic manipulation, VLAs lack mechanisms to quantify confidence in their predictions and to detect when their actions may be unreliable. This presents a critical limitation for real-world deployment in non-stationary environments, where models inevitably encounter scenarios outside their pretraining distribution and may fail without warning. To address this, we derive an efficient method for quantifying epistemic uncertainty in flow-matching models by leveraging velocity-field ...

8. `2606.18860v1` score=0.2593
   Title: Quantification of Uncertainty with Adversarial Models in Medical Image Segmentation
   Categories: cs.CV, cs.LG
   Abstract: Reliable pixel-level uncertainty quantification holds the potential to transform clinical workflows by enabling high-fidelity longitudinal monitoring and distinguishing true pathological changes from artifacts. Ideally, these models provide the stability required for critical treatment planning and surgical intervention. However, standard deep learning models often suffer from miscalibration, yielding overconfident predictions that mask underlying vulnerabilities at subtle pathological boundaries. To address this, we propose QUAM-SM, a post-hoc framework using targeted adversarial search to identify "adversarially fragile" pixels. By actively seeking perturbations that expose predictive inst...


## Candidate 017

Query: AI safety evaluation benchmark

Likely paper IDs:

1. `2606.07867v1` score=0.3297
   Title: The Cold-Start Safety Gap in LLM Agents
   Categories: cs.CL
   Abstract: Are tool-calling LLM agents equally safe throughout a conversation? We discover they are not: agents are most vulnerable at the very start of a session and become substantially safer after a few regular agentic tasks -- a phenomenon we term the cold-start safety gap. To study this systematically, we introduce Safety Over Depth for Agents (SODA), a benchmark that controls how many regular agentic tasks the agent completes before encountering a safety threat, supporting up to 20 preceding tasks. Evaluating 7 models from 4 families, safety improves by 9--52% as the number of preceding regular agentic tasks increases from zero to twenty. Representation analysis confirms that model hidden states ...

2. `2606.07874v1` score=0.3107
   Title: Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators
   Categories: cs.AI
   Abstract: LLMs-as-judges are the only way to evaluate safety at scale. Despite their importance, LLM-judges themselves are rarely evaluated beyond human agreement in simple, static benchmarks. We therefore investigate two under-explored but crucial properties of LLMs-as-judges: their susceptibility to relying on in context-information, and their steerability to differing safety definitions, which may not align with their internal safety priors. We evaluate the safety judging abilities of many generalist LLMs and safety-specific judges, and investigate the impact of task demonstrations, novel in-context information, and changing safety definitions. We find that while LLM-judges can learn from new infor...

3. `2606.15385v1` score=0.3075
   Title: Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds
   Categories: cs.AI
   Abstract: Reward hacking, where AI systems exploit misspecified objectives to achieve high reward without satisfying intended goals, remains a central challenge in AI safety. Yet most known instances have been discovered post hoc in frontier systems where controlled study is impractical. We adapt the AI Safety Gridworlds framework into a text-based evaluation suite that reformulates classic reinforcement learning safety tasks for language-based agents. Across frontier and mid-scale models, we find that specification gaming emerges zero-shot: models systematically achieve high observed reward while underperforming on hidden safety objectives, and even apparently safe behaviors can reflect misunderstand...

4. `2606.08531v1` score=0.3024
   Title: VESTA: A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents
   Categories: cs.AI
   Abstract: Large language models (LLMs) are increasingly evolving from simple text-based interaction systems into LLM agents that can maintain memory, use tools, access external environments, and execute tasks. As their capabilities and autonomy expand, the safety risks they face also become more diverse. Existing evaluations often rely on manually written scenarios, static prompts, or final-output judgments, making it difficult to capture the diverse risks that agents may face during task execution. We introduce VESTA, a fully automated scenario generation and safety evaluation framework for LLM agents. Based on five risk dimensions, VESTA instantiaes abstract and diverse safety risks in real-world ta...

5. `2606.20408v1` score=0.2736
   Title: LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems
   Categories: cs.CR, cs.AI
   Abstract: Large language model (LLM) agents are increasingly proposed as supervisory components for safety-critical systems, yet their robustness under sustained, adaptive adversarial pressure remains poorly characterized. We present NRT-Bench, a benchmark for multi-turn red-teaming of LLM agents acting as operators of a safety-critical system, instantiated in a simulated nuclear power plant control room. A five-role operator team, each backed by a configurable LLM, runs a plant governed by six critical safety functions (CSFs), while adversaries inject messages over four channels in bounded multi-turn sessions with per-turn feedback. Harm is an objective signal rather than LLM-judged text: a run termi...

6. `2606.11533v1` score=0.2661
   Title: AI Researchers Must Help Lead Arms Control to Mitigate Military AI Risks
   Categories: cs.CY, cs.AI, cs.ET, cs.LG
   Abstract: The advancement of AI capabilities compels researchers and the public to be more aware of its potential worldwide impact. A pressing near-term concern is the regulation of military AI applications. Armament manufacturers and defense contractors are increasingly investing in AI capabilities and forging partnerships with AI companies, creating a burgeoning coalition that demands military leaders, arms control diplomacy experts, and AI researchers collaborate to ensure a safer future. While AI researchers often focus on the long-term implications of superintelligent AI, this approach may not adequately address the immediate challenges posed by AI in military applications. Success requires ackno...

7. `2606.16808v1` score=0.2623
   Title: Adaptive and Explicit safe: Triggering Latent Safety Awareness in Large Reasoning Models
   Categories: cs.AI
   Abstract: While Large Reasoning Models (LRMs) excel at complex tasks, they remain highly vulnerable to sophisticated jailbreaks and direct harmful queries. To address this vulnerability, prior works depend heavily on external manual data annotation for safety alignment. However, we observe that LRMs can inherently identify safety risks when being re-presented with original queries alongside their own reasoning trajectories -- a capability we term Latent Safety Awareness. To leverage this safety awareness, we first employ Supervised Fine-Tuning (SFT) to explicitly induce safe tags to trigger safety analysis and guidance following the initial reasoning content for unsafe queries, while preserving standa...

8. `2606.08044v1` score=0.2439
   Title: When Behavioral Safety Evaluation Fails: A Representation-Level Perspective
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: Large Language Model (LLM) safety has often been evaluated at the behavior level, which provides limited evidence of internal robustness, as these evaluations target outputs rather than representation-level vulnerability under intervention. We formalize this discrepancy as the audit gap: the difference between behavioral safety and robustness under intervention. To study this gap, we construct dissociated models that preserve safe outward behavior while remaining vulnerable in the latent space. We introduce an intervention-based evaluation framework to test model robustness through soft interventions in parameter and latent spaces, including harmful fine-tuning and layer-wise latent perturba...


## Candidate 018

Query: alignment of large language models with human preferences

Likely paper IDs:

1. `2606.19057v1` score=0.2805
   Title: Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning
   Categories: stat.ML, cs.LG, stat.CO, stat.ME
   Abstract: Large Language Models (LLMs) are increasingly used as judges for scalable evaluation, yet such LLM--as--a--Judge systems exhibit systematic biases that are decoupled from semantic quality, most notably verbosity bias. Meanwhile, human supervision is costly and typically selective, yielding reliable positive judgments but leaving most outputs unlabelled and potentially mixed in quality. We formulate LLM evaluation under selective human supervision as a positive--unlabelled learning problem and propose a geometric auditing framework based on Partial Optimal Transport. By aligning a small set of human--verified positives with a reliable subset of unlabelled outputs in a fixed embedding space, o...

2. `2606.09124v1` score=0.2602
   Title: A Regret Minimization Framework on Preference Learning in Large Language Models
   Categories: cs.AI
   Abstract: Reinforcement learning with verifiable rewards (RLVR) has enabled progress on reasoning-intensive tasks by relying on task-specific verifiers that provide automated correctness signals. However, many realistic language tasks are difficult to equip with reliable verifiers, motivating a growing reliance on reinforcement learning from human feedback (RLHF). In this setting, we argue that a closer examination of how human feedback should be interpreted is essential. We introduce Regret-based Preference Optimization $(\textbf{RePO})$, which reframes RLHF through $\textit{regret minimization}$ rather than reward maximization. Human preferences are often shaped by $\textit{prospective}$ anticipatio...

3. `2606.13227v1` score=0.2424
   Title: PolyAlign: Conditional Human-Distribution Alignment
   Categories: cs.CL
   Abstract: Post-training methods such as supervised fine-tuning (SFT) and preference optimization typically align language models toward a single global assistant behavior. While effective for improving average helpfulness, this can suppress the natural variation of human responses across languages, tasks, and dialogue settings. We study this problem as conditional human-distribution alignment: models should match the human response distribution appropriate to the current interaction context, rather than a universal response style. We introduce PolyAlign, a distribution-aware alignment framework that organizes bilingual interaction data into bucket-specific human reference distributions defined by lang...

4. `2606.12754v1` score=0.2263
   Title: LLMs Can Better Capture Human Judgments--With the Right Prompts
   Categories: cs.CL, cs.AI
   Abstract: Are large language models (LLMs) bad at capturing human judgment? Two commonly stated limitations are that LLMs fail to capture full distributions of responses, and that their judgments are unstable across wording variations. We demonstrate simple prompting strategies that mitigate these limitations. Across two datasets--a U.S.-representative set of 144 moral scenarios and 38 moral beliefs from the International Social Survey Programme's Family and Changing Gender Roles module covering 32 countries--we show how simple elicitation techniques help improve AI-human alignment. First, prompting models to report standard deviations and response proportions recovers the full range of human response...

5. `2606.15315v1` score=0.2242
   Title: ChatPlanner: A Large Language Model Framework for Personalized Public Transit Routing
   Categories: cs.AI
   Abstract: Personalized public transit routing in public transit systems remains challenging due to the difficulty of capturing and integrating diverse user preferences into routing algorithms. This paper presents ChatPlanner, a novel framework that leverages Large Language Models (LLMs) to enable preference aware public transit routing. Our approach employs fine-tuned LLMs with Retrieval-Augmented Generation (RAG) to extract routing parameters and interpret nuanced user preferences from natural language queries, subsequently integrating these preferences into the objective function of a public transit routing algorithm. This study designs preference aware datasets incorporating eight personas and five...

6. `2606.07877v1` score=0.2221
   Title: Whose Norms? Disentangling Cultural and Personal Alignment in Large Language Models
   Categories: cs.CL
   Abstract: Large language models are increasingly used for social decision-making situations that require balancing cultural norms with personal preferences. For example, a user preferring honesty might ask whether to correct a coworker publicly when local norms favor indirect feedback. Yet existing research studies cultural alignment and personalization largely separately. We introduce PACT, the Personal-Preference and Cultural-Norm Trade-off framework, which evaluates whether models choose to follow a cultural norm or allow personal preferences. We find that LLMs vary in how rigidly they enforce cultural norms, with behavior shifted more by country context (7.8%) than age (1%) and gender (0.7%) and s...

7. `2606.19714v1` score=0.2188
   Title: AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing
   Categories: stat.ML, cs.AI, cs.LG, stat.CO, stat.ME
   Abstract: Large language models (LLMs) are increasingly used as judges for open-ended generation, as large-scale human evaluation is often expensive and difficult to scale, yet their preferences remain imperfect proxies for human judgment. Existing auditing pipelines often assume that a reliable subset of examples or clean supervision signals are available beforehand, for example from human annotation, heuristic filtering, or the outputs of strong judges. In LLM evaluation, this assumption is fragile: the initial split may inherit judge bias, while human verification is typically too scarce to define stable groups at scale. We propose AURA, an adaptive uncertainty--aware refinement framework for audit...

8. `2606.18656v1` score=0.2096
   Title: The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs
   Categories: cs.CL
   Abstract: Warning: This paper studies stereotypes and biases, and contains potentially disturbing examples, used for illustration purposes only. Our findings should not be interpreted as an argument against alignment. Instead, this paper highlights the need for principled approaches to more advanced alignment. Alignment aims to ensure that large language models (LLMs) behave safely and reliably, including by avoiding unsafe inferences. However, we show that such safety-oriented behaviors can misfire: models may reject warranted conclusions even when they are explicitly supported by context. We call this failure mode misfired alignment, where alignment-induced changes cause LLMs to override explicit ev...


## Candidate 019

Query: synthetic data generation for training language models

Likely paper IDs:

1. `2606.20400v1` score=0.3560
   Title: The Significance of Style Diversity in Annotation-Free Synthetic Data Generation
   Categories: cs.LG
   Abstract: Generating high-utility synthetic data for intent classification typically requires human-annotated seed data, which is often unavailable in fast-paced industrial settings. In this paper, we propose a framework for synthetic dialogue generation that works entirely without human-annotated data, relying solely on intent definitions. Our proposed dialogue generation framework utilizes two different types of topic and style attributes to improve data diversity. Also, we propose two novel post-hoc stylization models called Univ and Exam to transform synthetic LLM-generated utterances into more varied, human-like linguistic styles. To enhance data quality, we utilize an LLM-as-a-judge filtering pr...

2. `2606.19817v1` score=0.3123
   Title: Training-Free Metrics for Synthetic Object Detection Data: A Proxy for Detector Performance
   Categories: cs.CV
   Abstract: With the recent advent of image generative models, synthetic data are increasingly being used to supplement limited real datasets for training computer vision models. However, not all synthetic datasets improve performance equally, and their effectiveness can only be assessed by training a downstream model, which is computationally expensive and time-consuming. This problem is pronounced in the task of object detection, where the required annotations are much more dense due to bounding boxes. In this paper, we propose a pre-computable metric family, dubbed Conditional-Composition Domain Match (CCDM), which serves as a proxy for the relative utility of candidate synthetic training sets for do...

3. `2606.10802v1` score=0.3060
   Title: Boosting ECG Classification Performance by Pre-training with Synthesized Data
   Categories: cs.LG, cs.AI
   Abstract: Deep Neural Networks (DNNs) typically require extensive datasets for effective training. In the medical domain, acquiring large-scale data is often challenging due to privacy concerns and the rarity of certain diseases. To address this data scarcity, we investigate the efficacy of training DNN models using synthetic data, generated based on domain-specific medical knowledge. Specifically, we develop a knowledge-driven Gaussian-composition synthesis algorithm for single-lead II ECGs, in which each heartbeat is represented by Gaussian-shaped P, Q, R, S, and T wave components. Using this simulator, we generate synthetic data for four abnormal electrocardiogram (ECG) classes: atrial fibrillation...

4. `2606.16952v1` score=0.2907
   Title: Phantoms and Disclosures: a Causal Framework for Auditing Synthetic Data
   Categories: cs.LG, cs.AI, stat.AP, stat.ME, stat.ML
   Abstract: The rapid adoption of generative AI and Large Language Models (LLMs) has spurred interest in synthetic data as a privacy-preserving alternative to sensitive real-world datasets. However, generating high-utility synthetic data often carries the risk of memorizing and regurgitating private information from the training corpus. In this work, we present a customizable empirical auditing framework designed to detect and explain such data disclosures. Our framework introduces a mechanism to distinguish between "true disclosures"-where the system directly reproduces a user's information-and "phantom disclosures''-where the system incidentally generates a user's data. By partitioning input data into...

5. `2606.18389v1` score=0.2822
   Title: Want Better Synthetic Data? Steer It: Activation Steering for Low-Resource Language Generation
   Categories: cs.CL
   Abstract: Large language models (LLMs) have become an effective tool for synthetic data generation, including for low-resource languages, where generated data can improve downstream task performance. Current best-performing approaches typically rely on few-shot prompting with target-language examples, which increases inference costs and may reduce diversity through lexical anchoring. In this work, we investigate activation steering as an alternative for low-resource synthetic data generation. We study two steering strategies: Language Steering, which targets the linguistic identity of a language, and Quality Steering, which captures well-formedness by contrasting human-written and backtranslated text ...

6. `2606.18518v1` score=0.2821
   Title: PSyGenTAB: A Privacy-Preserving Framework for Synthetic Clinical Tabular Data Generation via Constrained Optimization
   Categories: cs.LG, cs.AI
   Abstract: The development of medical AI is constrained by limited access to high-quality clinical data due to institutional silos and strict privacy regulations such as HIPAA and GDPR. Synthetic data generation offers a potential solution, but existing methods lack principled mechanisms to explicitly manage the privacy-utility trade-off, often degrading clinically meaningful patterns or risking patient re-identification. We present PSyGenTAB, a privacy-preserving generative framework that formulates synthetic healthcare data generation as a constrained optimization problem solved using the Augmented Lagrangian Method. By embedding configurable privacy constraints directly into model training, PSyGenTA...

7. `2606.10481v1` score=0.2748
   Title: Advancing the State-of-the-Art in Empirical Privacy Auditing
   Categories: cs.LG, cs.AI, cs.CL, cs.CR, stat.ML
   Abstract: Parameter-efficient fine-tuning of large language models (LLMs) can exhibit problematic memorization of individual training examples. Empirical privacy auditing (EPA) quantifies this risk by measuring realistic data leakage on membership inference (MI) or reconstruction attacks. A key challenge in EPA is designing ``canary'' examples that are mixed with the privacy-sensitive training data. We propose generating synthetic canaries via high-temperature sampling ($T \geq 0.8$) from LLMs, using prompts tailored to the privacy-sensitive training data. These canaries act as high-influence outliers, ensuring high identifiability and hence strong audits. Further, since the canaries are themselves no...

8. `2606.18875v1` score=0.2712
   Title: Efficient Financial Language Understanding via Distillation with Synthetic Data
   Categories: cs.CL
   Abstract: Large instruction-following models are powerful but costly to deploy, particularly in finance, where labelled data are limited by confidentiality and expert annotation cost. We present an efficient framework for financial sentiment analysis through distillation with synthetic data, transferring knowledge from a large instruction-tuned teacher to compact student models. The framework is designed for low-resource conditions, where a small set of real examples are collected and labelled by hand. The framework then clusters the examples and uses the clusters to select seeds for generating synthetic examples via structured few-shot prompting. Experiments show that clustering-based seed selection ...


## Candidate 020

Query: data contamination detection in language model benchmarks

Likely paper IDs:

1. `2606.16524v1` score=0.4389
   Title: Neural Bayesian Anomaly Mitigation: A Robust Loss that Doubles as an Unsupervised Contamination Classifier
   Categories: cs.LG, astro-ph.CO, stat.ML
   Abstract: Engineered robust losses such as Huber, Student-$t$, and generalised cross-entropy make supervised models tolerant of contamination but cannot answer which observations are corrupted. We introduce Neural Bayesian Anomaly Mitigation (NBAM), a general-purpose drop-in loss derived from a Bayesian latent-switch mixture model: the marginal likelihood defines a robust supervised loss, and the associated posterior defines an unsupervised contamination classifier. Like Huber or Student-$t$, NBAM can replace the standard training loss in any supervised pipeline; unlike them, it additionally learns a structured contamination model and returns a calibrated per-sample contamination posterior. A learned ...

2. `2606.15547v1` score=0.3563
   Title: EcoBin: A Two-Stage Deep Convolutional Neural Network for Contamination-Aware Waste Classification
   Categories: cs.CV, cs.AI
   Abstract: Waste classification models have become highly accurate at sorting waste, often exceeding 95% on benchmark datasets. However, these models fail to account for contamination in recyclable waste. We present EcoBin, a two-stage deep convolutional neural network that classifies household waste by its disposal pathway and that explicitly accounts for contamination. The first stage is a base waste classifier built on an EfficientNetV2-S backbone that assigns each of the thirty waste categories in our dataset to one of four disposal pathways. The second stage is a contamination classifier that inspects any item routed toward recycling and overrides the decision to garbage when contamination is dete...

3. `2606.13120v1` score=0.2108
   Title: EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge
   Categories: cs.CL
   Abstract: Search Agents -- large language models augmented with search tools -- have intensified the need for future-proof evaluation benchmarks. Existing benchmarks such as BrowseComp rely on static knowledge, making them vulnerable to test-set contamination and parametric memorization. Consequently, models can achieve high scores through fact recall rather than genuine retrieval, obscuring true browsing competence via reasoning shortcuts. In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal. To collect these questions, we design a three-agent collaborative framework: (1) a QA synthesis ...

4. `2606.20502v1` score=0.1849
   Title: Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software
   Categories: cs.CR, cs.AI, cs.SE
   Abstract: Whether LLMs scoring well on vulnerability benchmarks genuinely reason about security or merely pattern-match on contaminated data remains unresolved. We present CWE-Trace, a framework for LLM vulnerability detection built from 834 manually curated Linux kernel samples spanning 74 CWEs. The framework enforces a strict temporal split (pre-2025 historical set / post-cutoff leakage-free set), preserves context-aware vulnerable--patched pairs, and introduces two diagnostic metrics: the Directional Failure Index (DFI) and Hierarchical Distance and Direction (HDD). We evaluate eight vanilla LLMs and 15 LoRA fine-tuned variants across non-targeted detection, targeted detection, and CWE classificati...

5. `2606.18729v1` score=0.1758
   Title: TimeLAVA: Learning-Agnostic Data Valuation for Time Series
   Categories: stat.ML, cs.LG
   Abstract: Data valuation quantifies the intrinsic quality of individual samples to enable principled data curation, quality control, and robust learning. For time series in critical domains such as healthcare, finance, and industrial monitoring, effective valuation methods are essential yet fundamentally lacking. Existing approaches are either model-dependent, limiting their generalizability, or designed for i.i.d. data and thus fail to capture temporal dependencies, multi-scale patterns, and non-stationary dynamics inherent to sequential data. We introduce TimeLAVA, a learning-agnostic framework that values temporal segments by their marginal contribution to minimizing distributional discrepancy betw...

6. `2606.07789v1` score=0.1755
   Title: A Framework for Evaluating and Benchmarking Concept Drift Detection Methods
   Categories: cs.LG, stat.ML
   Abstract: Data stream mining is fundamentally challenged by concept drift, where distributional changes can degrade model performance. Despite the proliferation of drift detection methods, progress in the field is hindered by inconsistent evaluation practices: studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection, making fair comparisons difficult. We address this gap with a novel benchmarking framework comprising three contributions: (1) a drift simulation method that injects controlled distributional changes into real-world datasets via Monte Carlo trials, enabling supervised evaluation while preserving real-world data...

7. `2606.08239v1` score=0.1676
   Title: When No Answer Is Correct: Diagnosing Absent Answer Detection for MLLMs in Video Understanding
   Categories: cs.AI, cs.CL, cs.CV
   Abstract: Multimodal large language models (MLLMs) have made substantial advancements in video understanding, yet the reliability of their responses remains underexplored. This work presents a diagnostic study of absent answer detection for MLLMs in video understanding, where the correct answer is deliberately excluded from the candidate set and a reliable model is expected to recognize that no valid option exists. We evaluate the absent answer detection behavior under three settings: multiple-choice questions augmented with an ``None of the Above'' option, open-ended generation with a detection instruction, and standard evaluation without any guidance. Across a diverse set of models and benchmarks, w...

8. `2606.08908v1` score=0.1587
   Title: Failure-Aware Refinement of Vision-Language Model for Lithography Defect Detection
   Categories: cs.CV, cs.AI
   Abstract: Semiconductor lithography inspection requires reliable detection of small pattern defects such as bridge, burr, pinch, and contamination. In this study, we propose a two-stage vision-language framework that combines initial defect detection with prediction refinement. In the first stage, Qwen3-VL is fine-tuned with LoRA as a vision-language adapter to predict defect counts, defect categories, and normalized bounding boxes from lithography images. However, direct fine-tuning may still produce common test-time errors, including false positives, missed defects, and incorrect defect types. To address this limitation, the second stage trains a refinement module using first-stage prediction failur...


## Candidate 021

Query: medical image segmentation with foundation models

Likely paper IDs:

1. `2606.16153v1` score=0.3831
   Title: A Comprehensive Survey of Medical Image Segmentation: Challenges, Benchmarks, and Beyond
   Categories: cs.CV, cs.AI
   Abstract: Medical image segmentation plays a critical role in clinical diagnostics, treatment planning, disease monitoring, and neurological disorder identification. This article presents a comprehensive review of its systematic development, covering widely used public datasets, representative methods built on the U-Net, Transformer, and SAM architectures, and key evaluation metrics with their differences, followed by an analysis of major challenges from multiple perspectives. Unlike surveys that focus on a single model family or a specific clinical application, this review organizes U-Net-, Transformer-, and SAM-based methods within a unified analytical framework, with a particular focus on their eff...

2. `2606.14754v1` score=0.3651
   Title: Sub-Semantic Image Segmentation
   Categories: cs.CV, cs.AI
   Abstract: Images can be segmented based on visual cues (i.e., texture segmentation) or into objects (i.e., semantic segmentation). We propose a new category of sub-semantic image segmentation that blurs the line between the two. In sub-semantic image segmentation, language is not used to name whole objects. Instead, it is used to partition an image into stable appearance patterns that can be described by language. To do that, we couple a general-purpose vision-language model to SAM 3, a promptable segmentation backbone whose native text pathway can ground rich descriptions into masks. Simple coupling fails for a number of reasons that we identify in the paper, and we overcome them by introducing DETEC...

3. `2606.16868v1` score=0.3269
   Title: Federated Medical Image Segmentation under Real-World Label Noise: A Benchmark Suite for Noisy Label Learning Method Selection
   Categories: cs.CV, cs.AI, cs.DC
   Abstract: While federated learning (FL) enables collaborative medical image segmentation without centralizing sensitive data, real-world deployment is frequently complicated by cross-site label imperfections such as contour disagreement, missing or additional structures, and confused labels. Federated noisy label learning (FNLL) aims to mitigate these effects, yet remains underused in practice as existing evidence is largely based on synthetic noise, simplified settings, and limited real-world noisy evaluation. We address this gap by introducing a benchmark suite that combines diverse real-world noisy datasets, deployment-relevant client-noise scenarios, and label-noise-targeted evaluation to support ...

4. `2606.16325v1` score=0.3157
   Title: Attention-Based Prototype Calibration for Multi-Rater Few-Shot Medical Image Segmentation
   Categories: cs.CV
   Abstract: Few-shot medical image segmentation methods typically assume a single ground-truth annotation, overlooking systematic variability across expert raters commonly observed in clinical datasets. We propose an attention-based prototype calibration framework for few-shot multi-rater segmentation that models rater-specific deviations from a consensus representation in prototype space. A lightweight yet principled attention operator directly refines rater prototypes without modifying the backbone feature extractor, making the approach fully compatible with existing prototype-based few-shot segmentation methods. This design preserves semantic consistency while enabling personalized segmentation outpu...

5. `2606.12371v1` score=0.2839
   Title: A Turbo-Inference Strategy for Object Detection and Instance Segmentation
   Categories: cs.CV
   Abstract: Object detection and instance segmentation tasks are closely related. Existing top-down instance segmentation methods usually follow a detect-then-segment paradigm, where an initial detector is used to recognize and localize objects with bounding boxes, followed by the segmentation of an instance mask within each bounding box. In such methods, the detection accuracy directly influences the subsequent segmentation performance. However, previous research has seldom explored the impact of the instance segmentation task on object detection. In this paper, we present a turbo-inference strategy for the top-down methods that leverages the complementary information between detection and segmentation...

6. `2606.18886v1` score=0.2621
   Title: DINO-Med3D: Bridging Dimension and Domain Gaps in Volumetric Segmentation via Progressive Adaptation
   Categories: cs.CV
   Abstract: Although DINOv3 has demonstrated remarkable semantic discrimination in natural imagery, its direct application to volumetric medical segmentation is hindered by inherent dimension and domain disparities. To resolve these issues, we propose DINO-Med3D, a two-stage progressive framework that repurpose the pre-trained DINOv3 encoder for 3D medical tasks. In the first stage, we mitigate the dimension gap by introducing a multi-slice embedding module that incorporates pseudo-3D context, while simultaneously employing a segmentation proxy task to adapt representations learned from natural scenes to the medical domain. Subsequently, we further enhance volumetric understanding by adding lightweight ...

7. `2606.15611v1` score=0.2617
   Title: Mutual Distillation of Dual-Foundation Models for Semi-Supervised PET/CT Segmentation
   Categories: cs.CV, cs.AI
   Abstract: Organ segmentation from PET/CT is critical for quantitative analysis and radiotherapy planning in oncology. To ease the high annotation cost of PET/CT segmentation, semi-supervised learning (SSL) provides a practical and effective solution for developing deep models with limited labeled data. Recent developments in visual foundation models have demonstrated remarkable adaptability with improved efficiency. In this work, we propose a mutual distillation framework that seamlessly exploits both structural and functional foundation models, which act as modality-specific generalists for distilling knowledge from structural CT and metabolic PET imaging. By bridging the gap between the task-specifi...

8. `2606.17958v1` score=0.2608
   Title: Beyond Visual Cues: CoT-Enhanced Reasoning for Semi-supervised Medical Image Segmentation
   Categories: cs.CV, cs.LG
   Abstract: Semi-supervised medical image segmentation has emerged as a dominant research problem in medical image analysis, mitigating annotation scarcity by leveraging consistency regularization on unlabeled data. However, existing approaches operate predominantly via visual pattern matching, relying heavily on pixel-level similarities. This visual-centric dependency often falters in clinical scenarios characterized by the visual-semantic mismatch, where visually similar lesions warrant distinct diagnostic conclusions, thus failing to capture the underlying diagnostic logic used by experts. To address this, we move beyond visual cues and propose CERS (CoT-Enhanced Reasoning Segmentation), a framework ...


## Candidate 022

Query: graph neural networks for scientific discovery

Likely paper IDs:

1. `2606.17185v1` score=0.3031
   Title: Finsler Geometry, Graph Neural Networks, and You
   Categories: cs.LG, eess.SP, math.DG, stat.ML
   Abstract: Graph neural network architectures based on the graph Laplacian approximate the Laplace-Beltrami operator, thus limiting their application to isotropic operators. As a nonlinear alternative to the Laplace-Beltrami operator, we consider estimates of the Finsler Laplacian on point clouds sampled from a manifold. We prove that these discrete estimates converge to the true operator on the manifold as the number of point samples grows. Moreover, we show that this operator can be expressed as a graph neural network layer, which we use to define a family of Finslerian graph neural networks constrained to express Finsler geometry. We show that Finslerian graph neural networks recover the geometry un...

2. `2606.09105v3` score=0.2778
   Title: Graph2Idea:Retrieval-Augmented Scientific Idea Generation with Graph-Structured Contexts
   Categories: cs.AI
   Abstract: Generating novel, feasible, and high-quality research ideas is an important yet challenging task in scientific discovery. Recent Large Language Model (LLM)-based methods often ground idea generation with retrieved literature, but the retrieved evidence is usually provided as flat text, such as titles, abstracts, or summaries. Such flat contexts may contain redundant or weakly relevant information, while making cross-paper relations among problems, methods, mechanisms, and findings difficult to identify and trace. To address this challenge, we propose Graph2Idea, a knowledge graph-guided framework for retrieval-augmented scientific idea generation.Graph2Idea first retrieves papers according t...

3. `2606.09638v1` score=0.2768
   Title: Data-driven discovery of governing differential equations across physical systems
   Categories: cs.LG, cs.SC, math-ph, physics.comp-ph, stat.AP
   Abstract: Differential equations play a critical role in scientific discovery because they provide a mathematical framework to describe the behaviour of physical phenomena. As a promising alternative to traditional first principles, data-driven differential equation discovery has attracted increasing attention for its ability to infer governing laws directly from experimental or simulated data, especially when the underlying physics is unclear. However, the field has expanded rapidly along diverse methodological directions, particularly with the emergence of AI-based approaches, and still lacks a clear organizing perspective. In this Review, we propose a problem-oriented perspective on data-driven dif...

4. `2606.10587v1` score=0.2740
   Title: Towards Diverse Scientific Hypothesis Search with Large Language Models
   Categories: cs.LG, cs.AI
   Abstract: Large language models (LLMs) are on the rise for accelerating scientific discovery, most recently in advanced tasks such as generating valid scientific hypotheses. Yet in many discovery settings, the goal is not to identify a single best hypothesis since validation can be noisy and expensive, and scientists benefit from a set of high-quality alternative hypotheses that hedge against downstream uncertainty for the best solutions. Nevertheless, commonly used evolutionary search recipes tend to prioritize optimization over exploration in hypothesis generation, and the resulting selection pressure during the search process leads to diversity collapse. Motivated by these limitations, we formulate...

5. `2606.12687v1` score=0.2736
   Title: Forecasting Is Not Attribution: Localizing Decoder Bypass in Graph-Based Neural Marketing Mix Models
   Categories: cs.LG
   Abstract: Marketing mix models are used to forecast business outcomes and to attribute those outcomes to marketing channels, but these goals are not equivalent. We study a failure mode in graph-based neural MMM called attribution bypass: a high-capacity decoder can obtain low forecasting error through target autoregression, dense communication, co-movement, context, or latent memory while failing to route counterfactual sensitivity through the graph used as the attribution object. We introduce DICE-MMM as a bounded diagnostic and training framework. We do not claim that observational neural MMM identifies causal effects. Instead, DICE separates three questions often conflated in graph-based MMM: graph...

6. `2606.13020v1` score=0.2724
   Title: SciR: A Controllable Benchmark for Scientific Reasoning in LLMs
   Categories: cs.AI
   Abstract: Three paradigmatic forms of inference recur across scientific reasoning: deduction, induction, and causal abduction. Reliably evaluating LLMs on these in scientific settings is currently out of reach: scientific benchmarks built on human annotations are costly and lack mechanistic ground truth, while synthetic logical-reasoning benchmarks do not resemble real scientific documents. We introduce SciR, a benchmark that combines multi-paradigm reasoning with controllable scientific rendering, anchored on three paradigmatic scientific problems. Tasks are generated from formal objects (deduction tree, inductive rule hypothesis, causal graph) to guarantee verifiable answers, then rendered into mult...

7. `2606.11560v1` score=0.2691
   Title: LLMs+Graphs: Toward Graph-Native, Synergistic AI Systems
   Categories: cs.DB, cs.AI
   Abstract: Large Language Models (LLMs) have advanced rapidly, but their limitations in structured and multi-hop reasoning underscore the need for graph-native, synergistic artificial intelligence (AI) systems. Graph-structured data underpins critical applications across social, biological, financial, transportation, web, and knowledge domains, making it essential to understand how LLMs can leverage graph computation for grounded, context-rich inference. Three complementary synergies are emerging: LLMs augmented with graph computation for retrieval and reasoning; bidirectional integration between LLMs and knowledge graphs (KGs), where LLMs support KG construction and curation while KGs enforce semantic...

8. `2606.17667v1` score=0.2573
   Title: Handling Feature Heterogeneity with Learnable Graph Patches
   Categories: cs.LG, cs.AI
   Abstract: In recent years, the rapid development of foundation models and graph pre-training technologies has spurred increasing interest in constructing a universal pre-trained graph model or Graph Foundation Model (GFM). However, a significant challenge is that existing models are unable to address feature heterogeneity in graph data without textual information, which hinders the transferability of graph models across different datasets. To bridge this gap, we propose the concept of learnable graph patches, which we regard as the smallest semantic units of any graph data. We decompose the graph into learnable graph patches by unfolding the node features and constructing corresponding patch structure...


## Candidate 023

Query: time series forecasting with transformers

Likely paper IDs:

1. `2606.16173v1` score=0.4855
   Title: TimeVista: Exploring and Exploiting Vision-Language Models as Judges for Time Series Forecasting
   Categories: cs.AI
   Abstract: High-quality time series forecasting is pivotal for real-world decision-making. However, traditional point-wise metrics often fail to reveal complex temporal patterns and align poorly with human intuitive preferences. While the ''LLM-as-a-Judge'' paradigm has revolutionized text evaluation by providing flexible, human-aligned judgment, its application to time series remains largely unexplored. In this paper, we leverage Vision-Language Models (VLMs) as judges for time series forecasting, harnessing their ability to comprehend time series plots grounded in textual information. Specifically, we propose a novel framework integrating micro- and macro-level judgments informed by contextual inform...

2. `2606.14941v1` score=0.4475
   Title: Semantics-Enhanced Retrieval-Augmented Time Series Forecasting
   Categories: cs.AI
   Abstract: Time series forecasting models often benefit from historical patterns. Inspired by Retrieval-Augmented Generation (RAG), recent research explored retrieving relevant historical time series segments to enhance forecasting. However, relying solely on time series similarity is often insufficient for retrieval under non-stationarity. To address this, we propose a multimodal approach: a \textbf{S}emantics-\textbf{E}nhanced \textbf{R}etrieval-\textbf{A}ugmented Time Series \textbf{F}orecasting framework, SERAF. Unlike mainstream approaches that depend only on time series similarity, SERAF conducts dual retrieval over the time series and their self-generated textual descriptions. It retrieves two c...

3. `2606.07291v1` score=0.4411
   Title: Trio: Learning Time-Series Forecasting with Temporal-Spatial-Sample Attention and Structural Causal Priors
   Categories: cs.LG
   Abstract: Multivariate time-series forecasting requires models to reason over temporal dynamics, cross-variable dependencies, and historical input-output correspondences. Recent Prior-Data Fitted Networks (PFNs) suggest that synthetic tasks can be useful for learning transferable inference behavior. However, directly transferring this paradigm to time-series forecasting remains difficult, since temporal order, dynamic lags, and recurring historical patterns are not naturally captured by ordinary tabular priors. Motivated by this observation, we propose Trio, a sample-aware time-series forecasting architecture based on Temporal-Spatial-Sample attention. Temporal attention captures within-window dynamic...

4. `2606.11746v1` score=0.3751
   Title: Time Series Analysis in Machine Learning
   Categories: astro-ph.IM, stat.ML
   Abstract: Time series analysis is a fundamental component of machine learning, especially in astrophysics and cosmology where temporal data abound. This chapter provides a pedagogical review of time series analysis techniques from a machine learning perspective. We cover the basic concepts of time series (stationarity, autocorrelation, seasonality), classical statistical models (autoregressive, moving average, ARIMA, exponential smoothing, state-space models), and modern machine learning approaches. In particular, we discuss how traditional statistical methods lay the groundwork, and then explore machine learning methods for time series, including feature-based regression, tree-based ensemble methods,...

5. `2606.10592v1` score=0.3579
   Title: Dirichlet-Guided Group Forecasting for Alleviating Over-smoothing in Time Series Forecasting
   Categories: cs.LG
   Abstract: Time series forecasting often suffers from over-smoothing, especially when future dynamics are multi-modal. Forecasts may follow the coarse trend of the observed future, but fail to preserve sharp changes, oscillations, turning points, and regime transitions that define plausible dynamic evolution. In this work, we revisit over-smoothing from the perspective of latent dynamical mode compression: under partial observation and single-realization supervision, multiple plausible future modes can be weakened, merged, or averaged during forecasting. Based on this view, we propose Dirichlet-Guided Group Forecasting (DGF), a mode-preserving forecasting framework that explicitly models multiple mode-...

6. `2606.12481v1` score=0.3515
   Title: Representing Time Series as Structured Programs for LLM Reasoning
   Categories: cs.LG, cs.AI
   Abstract: Large language models (LLMs) have demonstrated strong reasoning and instruction-following capabilities, making them potentially powerful tools for time-series analysis. However, time series lie outside their native textual modality, raising a fundamental question: how should time series be represented so that LLMs can reason about them effectively? Existing work typically serializes raw numerical sequences or fine-tunes pre-trained LLMs on time-series data. These approaches place the burden of extracting temporal structure directly on the LLM, creating a modality mismatch that often degrades performance on long sequences and introduces substantial computational overhead. In this work, we int...

7. `2606.15213v1` score=0.3413
   Title: Quantum-classical hybrid models based on error correction for time series forecasting
   Categories: quant-ph, cs.LG
   Abstract: Time series forecasting largely benefits from combining the strengths of different models, especially using a scheme where a model corrects another model by capturing supplementary patterns from forecasting errors. Concurrently, quantum models are providing a means to augment the classical capacity, including in time series forecasting, by acting alongside classical models in hybrid architectures. In this work, we propose the first forecasting system based on error correction that jointly uses quantum and classical models. Here, quantum models first extract patterns by exploring quantum phenomena, and classical models capture the remaining patterns from the quantum errors. Compared to classi...

8. `2606.18049v1` score=0.3357
   Title: ConTex: Reformulating Counterfactual Generation For Time Series Forecasting
   Categories: cs.LG
   Abstract: Decision-making with deep learning-based time series forecasting requires not only accurate predictions but also actionable insights. However, current architectures do not inherently provide such information. Specifically, guidance is needed on how current conditions must be modified to shift from a predicted outcome to a desired future scenario. Counterfactual explanations provide a natural framework for this task, as they represent minimal input changes that alter the model's prediction, indicating when and how intervention is required. Existing approaches rely on instance-wise optimization, leading to inconsistency across instances, high computational costs, and limited applicability in r...


## Candidate 024

Query: speech recognition with self supervised learning

Likely paper IDs:

1. `2606.11542v1` score=0.3800
   Title: Pretrained self-supervised speech models can recognize unseen consonants
   Categories: cs.CL, cs.AI
   Abstract: Modern pretrained self-supervised automatic speech recognition models are trained on large-scale audio data to encode speech into contextualized representations. However, their training data are heavily skewed toward high-resource languages with little data from low-resource languages, raising concerns about the potential underrepresentation of typologically uncommon speech sounds such as click consonants primarily found in Khoisan languages. This leads to our central research question: Can these models recognize click consonants as accurately as other speech sounds? To address this question, we fine-tune and compare pretrained self-supervised speech models (Wav2Vec2 and HuBERT) on data from...

2. `2606.19793v1` score=0.3477
   Title: Systematic Study of Dysarthric Speech Recognition: Spectral Features and Acoustic Models
   Categories: eess.AS, cs.AI, cs.LG, cs.SD, eess.SP
   Abstract: The challenge associated with recognizing dysarthric speech primarily arises from pronounced acoustic variability attributed to impaired articulatory precision. Past research has demonstrated improved recognition through the use of hybrid DNN/HMM sequence discriminative training. This paper presents a comprehensive investigation of various combinations of acoustic features tailored to different Acoustic Models, offering suitable feature selections for each. The incorporation of Pitch features notably improved recognition performance, especially for sentence recognition tasks involving dysarthric speech. Through a systematic examination of the TORGO database, we have demonstrated the potentia...

3. `2606.15059v1` score=0.3293
   Title: A Practical Evaluation Method for Long-Form Simultaneous Speech-to-Speech Translation
   Categories: cs.CL
   Abstract: Simultaneous speech-to-speech translation (SimulS2ST) enables real-time cross-lingual communication, but existing evaluation has focused largely on short or pre-segmented speech rather than long-form, continuous input. Prior approaches are difficult to reproduce and make assumptions that do not hold for end-to-end systems. We present a practical evaluation method for long-form SimulS2ST. Given source speech, pre-segmented source transcripts, and reference translations, we run automatic speech recognition (ASR) and forced alignment on the generated target speech to recover token-level timestamps, then apply a sentence-embedding-based aligner to match the target text to its corresponding sourc...

4. `2606.14639v1` score=0.3213
   Title: From Self-Supervised Speech Models to Mixture-of-Experts for Robust Anti-Spoofing
   Categories: cs.SD, cs.AI
   Abstract: Recent advances in speech generation have significantly improved the naturalness of synthetic speech, making spoofing detection increasingly challenging. A key limitation of current anti-spoofing systems is their limited robustness to unseen synthesis methods. In this work, we transform a self-supervised speech representation model into a Mixture-of-Experts (MoE) architecture to improve generalization. Feed-forward blocks in selected encoder layers are replaced by multiple expert networks controlled by a layer-wise gating mechanism, allowing experts to capture complementary acoustic patterns while preserving the representations learned during self-supervised pretraining. We further analyze t...

5. `2606.19791v1` score=0.3142
   Title: Cross-Dataset, Age, and Gender Generalization: A Comprehensive Analysis of Fine-Tuning Strategies for Low-Resource Children's ASR
   Categories: eess.AS, cs.AI, cs.SD
   Abstract: The challenge associated with recognizing dysarthric speech primarily arises from pronounced acoustic variability attributed to impaired articulatory precision. Past research has demonstrated improved recognition through the use of hybrid DNN/HMM sequence discriminative training. This paper presents a comprehensive investigation of various combinations of acoustic features tailored to different Acoustic Models, offering suitable feature selections for each. The incorporation of Pitch features notably improved recognition performance, especially for sentence recognition tasks involving dysarthric speech. Through a systematic examination of the TORGO database, we have demonstrated the potentia...

6. `2606.13507v1` score=0.3117
   Title: Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data
   Categories: cs.CL
   Abstract: Large-scale mined corpora provide abundant training data for end-to-end speech-to-speech translation (S2ST) but may contain noise, misalignment, and semantic errors. Filtering noisy data is crucial to maintain robust speech translation performance. We study how to train an audio-language model to make keep/drop decisions on paired speech directly from audio. To obtain reliable supervision without manual labels, we adopt a scalable two-stage Rank-to-Distill strategy. A lightweight ranker generates keep/drop pseudo-labels from noisy speech pairs, then trains an audio large language model to predict keep/drop directly from raw paired speech. The resulting model jointly captures acoustic fidelit...

7. `2606.18645v1` score=0.3002
   Title: Augmenting Dysarthric Speech Severity Assessment with MOS Supervision
   Categories: eess.AS, cs.AI
   Abstract: Dysarthria is a speech disorder marked by reduced intelligibility and communicative effectiveness. Automatic utterance-level assessment of dysarthric speech can support scalable speech monitoring and therapy-related analysis. Yet training such systems is bottlenecked by the scarcity of clinically annotated dysarthric speech. This work proposes to augment dysarthric speech assessment using data from speech synthesis evaluations, specifically human-annotated utterances with Mean Opinion Score (MOS) labels from the QualiSpeech corpus. Experiments show that fine-tuning on speech synthesis assessment data consistently improves performance on both intelligibility and naturalness prediction, while ...

8. `2606.11033v1` score=0.2899
   Title: AuRA: Internalizing Audio Understanding into LLMs as LoRA
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: Recent efforts to extend large language models (LLMs) to speech inputs typically rely on cascaded ASR-LLM pipelines, end-to-end speech-language models, or bridge/distillation-based adaptation. While these routes respectively reuse strong pretrained components, enable native speech-language interaction, or offer lightweight adaptation, they often suffer from transcript-interface latency, costly multimodal training, or sequential speech-language coupling. To address these limitations, we present AuRA, a method that distills audio encoding capability into the LLM. Specifically, AuRA feeds the same speech input to an ASR encoder (as a teacher) and a LoRA-adapted LLM (as a student) through a ligh...


## Candidate 025

Query: code generation benchmark for large language models

Likely paper IDs:

1. `2606.15500v1` score=0.2872
   Title: LLM4RTL: Tool-Assisted LLM for RTL Generation
   Categories: cs.AR, cs.AI, eess.SY
   Abstract: Large language models (LLMs) have facilitated impressive progress in software engineering, code generation, tooling, and systems. Concurrently, a significant body of research has developed which explores a growing variety of methods and systems for applying LLMs to hardware and chip design (e.g., systems for RTL code generation based on functional description). However, when it comes to open Verilog/RTL code-generation, we need high-quality training samples to build specialized and more effective LLM systems through fine-tuning or low-rank adaptation. Here, we propose a ``judge-renew-check-renew-check'' (JRCRC) pipeline which updates a current public dataset using a hierarchy of state-of-the...

2. `2606.09577v1` score=0.2820
   Title: Code Is More Than Text: Uncertainty Estimation for Code Generation
   Categories: cs.CL, cs.LG, cs.SE
   Abstract: Large language models (LLMs) are increasingly deployed as code generators, where silently wrong programs pose real safety and reliability risks. Reliable uncertainty estimation (UE) is essential for selective prediction, human-in-the-loop review, and downstream agentic decisions. Yet most existing code UE methods are inherited from natural language (NL) generation and ignore properties that make code distinct. We argue that code differs from NL in three ways: a single wrong token can break an entire program (token fragility); algorithmic intent and concrete implementation can disagree independently (intent-code gap); and programs can be executed (executability). We instantiate these properti...

3. `2606.15589v1` score=0.2728
   Title: Is Code Better Than Language for Algorithmic Reasoning
   Categories: cs.LG, cs.AI
   Abstract: For tool-augmented language models, comparing natural-language reasoning with code-execution pipelines is difficult because the comparison changes both the intermediate representation and the execution mechanism. We separate these factors with an intermediate intervention: the model expresses its reasoning as executable code, and the language model simulates that code in context to produce an answer. On a 40-task verifiable algorithmic benchmark, deterministic code execution outperforms natural-language reasoning by +31.6pp. We observe that the intermediate intervention is not meaningfully different from natural-language reasoning (+0.15pp). These results suggest that, in our evaluated setti...

4. `2606.12620v1` score=0.2679
   Title: HybridCodeAuthorship: A Benchmark Dataset for Line-Level Code Authorship Detection
   Categories: cs.SE, cs.AI
   Abstract: Thanks to the rapid adoption of AI code assistants powered by large language models (LLMs), industry codebases are, increasingly, a hybrid of AI- and human-authored code. For risk management and productivity analysis purposes, it is crucial to enable fine-grained location detection of AI-generated code. To develop algorithms for this task, quality benchmarks are needed to assess performance. However, existing benchmarks tend to comprise academic, LeetCode-style problems and presume a code snippet is either completely human-authored or completely AI-authored, which is not reflective of the diverse intents and styles of industry codebases utilizing AI code assistants. To fill these gaps, we in...

5. `2606.17514v1` score=0.2331
   Title: Unlocking LLM Code Correction with Iterative Feedback Loops
   Categories: cs.SE, cs.AI
   Abstract: Large Language Models have shown remarkable capabilities in code generation. However, most existing evaluations focus only on single-attempt accuracy and overlook the iterative refinement process that is central to real-world programming. This study presents a systematic investigation of LLMs' ability to rectify their own code through execution feedback. Using real-world programming problems across four models and two major programming languages, this study evaluates performance using iterative refinement framework where LLMs receive compiler error messages and testcase feedback after each attempt. This study introduces metrics to evaluate code failures, analyze rectification patterns, and c...

6. `2606.20100v1` score=0.2273
   Title: WeGenBench: A Multidimensional Diagnostic Benchmark towards Text-to-Image Model Optimization
   Categories: cs.CV
   Abstract: Recent text-to-image generation models have demonstrated remarkable capabilities in synthesizing highly realistic images from text inputs alone. Although existing benchmarks can evaluate the generation capabilities of various models to some extent, they struggle to comprehensively and accurately measure performance across multiple dimensions, often failing to reveal the inherent deficiencies of models in specific categories. To address these limitations, we propose WeGenBench, a novel benchmark designed for the comprehensive, multi-perspective evaluation of text-to-image generation capabilities. Our benchmark comprises a total of 4,000 test prompts across two primary categories, meticulously...

7. `2606.08676v1` score=0.2203
   Title: Lost in the Flow with Code Talkers: Unveiling the Instruction-Tuning Tax of Large Language Models in Code Tasks
   Categories: cs.SE, cs.AI, cs.CL
   Abstract: AI coding assistants have significantly improved developer productivity by automatically suggesting code that aligns with user intent, and many of these tools are now integrated directly into Integrated Development Environments (IDEs). Developers interact with code in two distinct cognitive modes: Flow and Command. While developers require tools that directly complete or infill code in unfinished programs during Flow mode, they also need tools that can comprehend intentions expressed as natural-language instructions and convert them into executable code in Command mode. Although instruction-tuned Large Language Models (LLMs) dominate many application scenarios due to their abilities to infer...

8. `2606.15932v2` score=0.2045
   Title: Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence
   Categories: cs.CL
   Abstract: While Large Language Models (LLMs) have substantially advanced text-to-code synthesis, many real programming tasks specify intent through visual artifacts such as screenshots, charts, vector drawings, videos, and interactive states. These tasks require models to connect visual perception to executable programs, because correctness depends not only on syntax but also on layout, data semantics, interaction behavior, and domain-specific constraints that apply after execution. This survey examines Multimodal Code Intelligence, covering systems that generate, edit, refine, or reason with code under visually grounded inputs and outputs. We first formulate the field by the role that code plays in e...


## Candidate 026

Query: mathematical reasoning in large language models

Likely paper IDs:

1. `2606.17289v1` score=0.4178
   Title: Nothing from Something: Can a Language Model Discover 0?
   Categories: cs.AI, cs.CL
   Abstract: AI systems based on artificial neural networks are being developed with aspirations of pushing the boundary of human mathematical knowledge. A key question for these systems is how much they can reach beyond their training data. Mathematical discovery requires a strong form of out of distribution generalization; the ability to hypothesize genuinely new - and potentially logically more powerful - mathematical structures. It has been hypothesized that language abilities support such generalizations in human cognition. In this work, we use simple arithmetic as a case study for examining how modern AI models could expand their mathematical horizons, evaluating whether these models can independen...

2. `2606.11470v1` score=0.3889
   Title: The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes
   Categories: cs.CL
   Abstract: Large Language Models (LLMs) have achieved strong performance across natural language processing tasks, yet reliable reasoning remains an open challenge. Although modern LLMs show progress in structured inference, multi-step problem solving, and contextual understanding, their reasoning behavior is often inconsistent and sensitive to prompting strategies, task design, and model scale. This survey provides a systematic analysis of more than 300 recent papers from arXiv, Semantic Scholar, Google Scholar, Papers with Code, and the ACL Anthology to examine how reasoning capabilities emerge in LLMs and where they fail. We make three main contributions. First, we introduce a structured taxonomy of...

3. `2606.09585v1` score=0.3476
   Title: Optical Reasoning: Rethinking Images as an Expressive Reasoning Medium Beyond Text
   Categories: cs.AI
   Abstract: Chain-of-Thought (CoT) improves the performance of Large Language Models (LLMs) and has been extended to Multimodal Large Language Models (MLLMs). More recent work further moves from text-based multimodal reasoning toward interleaved-modal reasoning, where intermediate steps can incorporate both textual rationales and visual evidence. In this work, we propose a bolder and more ambitious idea: could images alone serve as the reasoning medium for both language and multimodal tasks? To explore this, we propose optical reasoning, which treats images as a standalone reasoning medium. We instantiate this concept with two variants: typographic-based optical reasoning, which optimizes visual layouts...

4. `2606.16152v1` score=0.3210
   Title: The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematical Reasoning
   Categories: cs.AI
   Abstract: Knowledge distillation from powerful reasoning models is widely used to improve Small Language Models (SLMs) on mathematical reasoning, often assuming that traces with higher reward model scores provide more useful supervision. We identify a counterintuitive \textbf{Quality-Utility Paradox} in mathematical reasoning distillation. Data refined or synthesized by a stronger Oracle obtains higher perceived quality according to reward models, yet consistently underperforms traces generated by the SLM itself and selected through rejection sampling across Qwen2.5, LLaMA-3, and DeepSeek families. Our analysis shows that Oracle refinement couples logical repair with distributional drift away from the...

5. `2606.13782v2` score=0.3123
   Title: MA-ProofBench: A Two-Tiered Evaluation of LLMs for Theorem Proving in Mathematical Analysis
   Categories: cs.AI
   Abstract: Large Language Models (LLMs) have made notable progress in automated theorem proving, yet existing formal benchmarks remain limited in both mathematical coverage and difficulty. Most are concentrated in areas that are easier to formalize, such as algebra and elementary number theory, and provide limited coverage of subfields that require deeper reasoning, including mathematical analysis. To address this gap, we introduce MA-ProofBench, to the best of our knowledge, the first formal theorem-proving benchmark dedicated to Mathematical Analysis. The benchmark contains 200 formalized theorems covering 6 core topics and 27 subcategories, including measure and integration theory, complex analysis,...

6. `2606.18453v1` score=0.3029
   Title: LLM Parameters for Math Across Languages: Shared or Separate?
   Categories: cs.CL
   Abstract: Large language models (LLMs) exhibit substantial cross-lingual variation in mathematical reasoning performance, but it remains unclear whether these differences reflect language-specific parameters or a shared mechanism that manifests differently by language. We present a cross-lingual mechanistic analysis of mathematical reasoning in LLMs, enabling us to localize and compare model parameters that support mathematical reasoning across languages. We find that the extracted math-associated parameters exhibit partial cross-lingual overlap, with the strongest overlap concentrated in intermediate model layers. We further observe that English consistently produces the largest set of math-relevant ...

7. `2606.15080v1` score=0.2837
   Title: AdaMame: A Training Recipe for Adaptive Multilingual Reasoning
   Categories: cs.CL, cs.AI
   Abstract: While Large Reasoning Models (LRMs) show strong performance in English, they often fail to reason in the language of the query, a phenomenon known as language collapse. Existing RL-based fixes typically add a binary language fidelity reward to the accuracy objective, yet still incur trade-off in accuracy, mid-trace code-switching, and excessive token usage. In this work, we propose AdaMame, a two-stage training recipe for multilingual mathematical reasoning that addresses these limitations by adaptively aligning the reasoning language to the query language without compromising accuracy. The first SFT stage fine-tunes on naturally occurring reasoning traces across five languages to establish ...

8. `2606.17524v1` score=0.2821
   Title: Learning to Refine Hidden States for Reliable LLM Reasoning
   Categories: cs.LG
   Abstract: Large language models show strong reasoning ability, but their internal reasoning process can remain unstable in complex multi-step settings, where early hidden-state errors may propagate to incorrect predictions. We propose ReLAR, a reinforcement-guided latent refinement framework that iteratively updates hidden representations before decoding. ReLAR maintains a compact latent reasoning state and uses learned depth and action controllers to adaptively determine both the number and direction of refinement steps. The controllers are trained with a policy gradient objective based on step-wise likelihood improvement, enabling efficient input-dependent reasoning without explicit chain-of-thought...


## Candidate 027

Query: tool use planning for language model agents

Likely paper IDs:

1. `2606.11652v1` score=0.3486
   Title: IAPO: Input Attribution-Aware Policy Optimization for Tool Use in Small Multimodal Agents
   Categories: cs.LG
   Abstract: This paper investigates reinforcement learning (RL) methods for improving tool-calling capabilities in multimodal small language model (SLM) agents. While existing works have explored various reward designs to improve agentic tool-calling ability, these approaches face inherent limitations for SLM training, especially under multimodal scenarios. First, many existing methods evaluate tool use correctness through exact matching against certain ground-truth or predefined formats. However, this assumption is often unsuitable for multimodal tasks, where multiple tool use paths may be valid and annotated tool trajectories are typically unavailable. Second, such sparse and brittle binary rewards pr...

2. `2606.16591v2` score=0.3125
   Title: SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents
   Categories: cs.CL
   Abstract: Large language model (LLM) agents increasingly rely on agent harnesses that manage context, tools, and multi-turn execution, making tools a central interface for acting in realistic digital environments. As harness-connected tool ecosystems expand to hundreds or thousands of APIs, services, and task-specific skills, exhaustive tool schema injection becomes costly and imposes a closed-world assumption that limits agents to a predefined static inventory. Retrieval-augmented tool selection offers a natural alternative, but existing one-shot retrieval methods often fail to align isolated tool descriptions with the agent's true task intention, especially in long-horizon tasks where required capab...

3. `2606.08300v1` score=0.2928
   Title: QueryWeaver: Reliable Multi-Tool Query Execution Planning via LLM-Based Graph Generation
   Categories: cs.LG
   Abstract: Many real-world queries over personal data span multiple applications and require structured planning, as individual tools expose only partial information. While LLMs show strong reasoning and tool use, reliably executing multi-step, cross-tool queries remains challenging. We introduce a system that converts natural language queries into structured graphs and executes them via a deterministic planner. Our approach uses depth-first search to resolve dependencies and combine results across tools, improving reliability and enabling queries beyond traditional keyword-based search. We demonstrate high accuracy even with smaller or locally hosted LLMs.

4. `2606.15508v1` score=0.2928
   Title: ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents
   Categories: cs.AI
   Abstract: Tool-augmented large language model agents increasingly operate over large tool libraries, but existing evaluations often focus on whether a model can call a tool correctly rather than how the visible tool menu shapes reliability, efficiency, and safety-relevant risk exposure. We introduce ToolMenuBench, a benchmark for evaluating tool-menu construction in multi-step LLM agents. ToolMenuBench varies tool-menu size, distractor type, state-dependent task structure, and risk exposure, and reports both filter-level and downstream agent metrics, including visible-tool count, risky-tool exposure, task success, wrong-tool calls, premature actions, and token usage. In a controlled evaluation across ...

5. `2606.11702v1` score=0.2856
   Title: MedCTA: A Benchmark for Clinical Tool Agents
   Categories: cs.CV, cs.AI, cs.CL
   Abstract: To make clinically grounded decisions, medical AI agents are expected to go beyond simple recognition and be capable of tool retrieval, evidence acquisition, and integration. Existing benchmarks largely evaluate isolated perception or single-turn question answering, and therefore provide limited visibility into failures of planning, tool recruitment, and rollout reliability. We introduce MedCTA, a benchmark for evaluating medical tool agents on clinician-validated, step-implicit tasks grounded in realistic multimodal clinical inputs, including radiology images, pathology slides, and reports. MedCTA comprises 107 real-world clinical tasks with clinician-verified executable trajectories over 5...

6. `2606.09032v1` score=0.2829
   Title: Bridging the Agent-World Gap: Text World Models for LLM-based Agents
   Categories: cs.CL
   Abstract: Large language model (LLM)-based agents are increasingly used in interactive textual environments, from web navigation and code editing to tool use and long-horizon dialogue. Yet many remain largely reactive, mapping observations to actions without an explicit model of how these environments are structured and evolve. This motivates text world models (TWMs): transition models over textual states that, given a state and a candidate action, predict the resulting webpage, terminal output, API response, or user reply, thereby supporting planning, efficient learning, and principled evaluation. We systematically review text world models for LLM-based agents, organized around a formal framework and...

7. `2606.16274v1` score=0.2787
   Title: GraphWorld: Long-Horizon Planning with World Models for End-to-End Autonomous Driving
   Categories: cs.CV
   Abstract: End-to-end autonomous driving has made significant progress by unifying perception, prediction, and planning within a single learning framework, achieving strong performance in short-horizon decision making. However, most existing E2E-AD methods remain confined to short-horizon planning and lack the ability to model long-term temporal dependencies, which severely limits their generalization and security in complex and highly interactive driving scenarios. In this work, we propose GraphWorld, an E2E-AD framework that explicitly enhances long-horizon planning through latent world modeling. We introduce an Ego-Centric Interaction Graph, which adaptively models critical neighboring agents based ...

8. `2606.13663v1` score=0.2786
   Title: HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents
   Categories: cs.CL
   Abstract: Tool-augmented LLM agents commonly rely on step-wise atomic tool calls, where each invocation, observation, and value transfer is exposed in the main reasoning trace. This creates an \emph{execution-granularity mismatch}: locally deterministic tool workflows are unfolded into repeated model-visible decisions, consuming context and forcing the model to manage low-level dataflow in the trace. We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution. A model invokes HyperTool with a code block that can call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally, ...


## Candidate 028

Query: semantic search with dense retrieval and sparse retrieval

Likely paper IDs:

1. `2606.17910v1` score=0.3658
   Title: Non-negative Elastic Net Decoding for Information Retrieval
   Categories: cs.IR, cs.AI, cs.CL
   Abstract: Dense retrieval has become the dominant paradigm in information retrieval, in which each document is scored against a query by the inner product of their vector embeddings, and the top-$k$ documents by score are retrieved for this query. However, since each document's score depends solely on the embedding of the query and itself, the retrieval process is oblivious to the content of the entire corpus. Therefore, dense retrieval cannot avoid selecting semantically similar documents from the corpus, which may result in a non-diverse, redundant set of retrieved documents. To this end, we approach retrieval as a joint decoding problem, in which documents are selected as a set with regard to the c...

2. `2606.11945v1` score=0.3416
   Title: uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking
   Categories: cs.CL, cs.IR
   Abstract: This report describes our participation in SemEval-2026 Task 8 on multi-turn retrieval and question answering. The task evaluates conversational systems across four domains (finance, cloud documentation, government, Wikipedia), and includes unanswerable queries where the available collection does not contain sufficient evidence to produce a complete response. We propose a multi-turn retrieval-augmented generation pipeline that combines learned sparse retrieval with LLM-based reranking and generation. Using sparse retrieval as the primary retrieval method, we leverage its strong generalization across domains. In addition, we make use of the long-context capabilities of LLMs for conversational...

3. `2606.10621v1` score=0.2979
   Title: STORM: Stepwise Token Optimization with Reward-Guided Beam Search
   Categories: cs.IR, cs.AI
   Abstract: Modern retrieval increasingly relies on dense and learned-sparse neural models that are effective but require encoding the entire corpus into a specialized index, rebuilt whenever the model changes. Lexical retrievers like BM25 stay efficient and transparent on a standard inverted index that need not change as models evolve, but suffer from vocabulary mismatch. LLM query rewriting can help, yet prompted rewriters emit well-formed but retrieval-ineffective or harmful-terms, and training against a retrieval reward gives only delayed, sequence-level supervision that obscures which terms helped. We introduce STORM (Stepwise Token Optimization with Reward-guided beaM search), a self-supervised fr...

4. `2606.11350v1` score=0.2897
   Title: When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval
   Categories: cs.CL, cs.IR
   Abstract: Retrieval-augmented generation degrades when scaled to large, heterogeneous document collections, where dense similarity loses discriminative power, and top-k retrieval increasingly returns semantically similar but contextually incorrect chunks. We refer to this failure mode as vector search dilution. Even when using hybrid dense+sparse retrieval, we observed this firsthand in a deployed Wyoming Department of Transportation corpus, where scaling from 54 to 1,128 documents (88,907 chunks) reduced accuracy from 75% to below 40%. To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones...

5. `2606.12294v1` score=0.2886
   Title: Bridging the Modality Gap in Forensic Image Retrieval
   Categories: cs.CV, eess.IV
   Abstract: Automated image retrieval plays an increasingly critical role in modern forensic analysis, supporting investigative workflows that rely on efficient comparison of visual evidence. While prior work has focused primarily on developing and optimizing multimodal retrieval systems, limited attention has been paid to evaluating the forensic applicability of these technologies across diverse real-world scenarios. In this study, we present a unified retrieval framework adapted to four key forensic tasks: (1) tattoo image retrieval given a tattoo query image; (2) tattoo retrieval guided by human-expert textual descriptions, modelling the common situation where a witness verbally describes a tattoo; (...

6. `2606.11265v1` score=0.2863
   Title: When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines
   Categories: cs.CR, cs.AI
   Abstract: Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection. Existing studies mainly evaluate poisoning under simplified retrieval settings, overlooking practical RAG pipelines involving document chunking, dense retrieval, reranking, and grounded generation. In this paper, we revisit corpus poisoning under realistic multi-stage retrieval pipelines and show that many existing attacks substantially degrade after reranking despite achieving high retrieval-stage relevance. We identify retrieval granularity mismatch as a key reason for this failure: document-level adversarial signals are oft...

7. `2606.18508v1` score=0.2847
   Title: MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval
   Categories: cs.CL, cs.IR
   Abstract: Retrieval-augmented generation (RAG) systems depend critically on how documents are chunked and searched. Fine-grained chunks can improve retrieval precision but expand the search space, increasing latency and cost; larger chunks reduce the number of candidates but make dense similarity less reliable, as the representation for each chunk mixes multiple topics and introduces more semantic noise. This trade-off becomes especially limiting in deep research tasks, where retrieval must be both fast and precise across large, heterogeneous corpora. We introduce MCompassRAG, a metadata-guided retrieval framework that uses topic-level signals as a semantic compass for selecting relevant evidence. Ins...

8. `2606.14269v1` score=0.2801
   Title: ScoreGate: Adaptive Chunk Selection for Retrieval-Augmented Generation via Dual-Score Statistical Fusion
   Categories: cs.IR, cs.CL
   Abstract: Fixed-cardinality retrieval injects a constant top-K chunks into the generator regardless of query complexity, causing over-retrieval for narrow queries and under-retrieval for compositional ones. We describe ScoreGate, a lightweight score-space decision mechanism that controls retrieval cardinality at inference time using two scores already produced by the standard pipeline: bi-encoder similarity s_i and cross-encoder reranker score r_i, with no additional model inference calls required. Its core insight is that cross-encoder affirmation can rescue semantically relevant chunks that bi-encoder retrieval ranks poorly due to vocabulary mismatch -- a failure mode unaddressed by fixed-K or singl...


## Candidate 029

Query: cross lingual information retrieval

Likely paper IDs:

1. `2606.18033v1` score=0.4194
   Title: When English Isn't the Best Teacher: Source Language Effects in Cross-Lingual In-Context Learning
   Categories: cs.CL, cs.AI
   Abstract: Cross-lingual transfer in multilingual NLP has been widely explored in supervised fine-tuning contexts, where factors like data availability and linguistic similarity largely determine transfer quality. As the field shifts toward few-shot In-Context Learning (ICL), it is often presumed that insights from fine-tuning carry over unchanged. Yet this assumption has not been rigorously evaluated, leaving open the question of how to choose source languages for cross-lingual ICL. We conduct a broad empirical study of cross-lingual transfer in ICL spanning seven tasks, six models, and a typologically diverse set of languages. We further analyze language confusion, a key obstacle for generative tasks...

2. `2606.18453v1` score=0.3481
   Title: LLM Parameters for Math Across Languages: Shared or Separate?
   Categories: cs.CL
   Abstract: Large language models (LLMs) exhibit substantial cross-lingual variation in mathematical reasoning performance, but it remains unclear whether these differences reflect language-specific parameters or a shared mechanism that manifests differently by language. We present a cross-lingual mechanistic analysis of mathematical reasoning in LLMs, enabling us to localize and compare model parameters that support mathematical reasoning across languages. We find that the extracted math-associated parameters exhibit partial cross-lingual overlap, with the strongest overlap concentrated in intermediate model layers. We further observe that English consistently produces the largest set of math-relevant ...

3. `2606.15345v2` score=0.3110
   Title: Beyond Monolingual Deep Research: Evaluating Agents and Retrievers with Cross-Lingual BrowseComp-Plus
   Categories: cs.CL, cs.IR
   Abstract: Deep research agents are increasingly evaluated on their ability to search for evidence, reason over retrieved sources, and produce grounded answers. Existing browsing benchmarks, however, largely assume that the user's query and the supporting evidence are written in the same language, leaving open whether agentic search systems can operate when relevant evidence appears in another language. We introduce XBCP (Cross-lingual BrowseComp-Plus), a controlled benchmark that preserves the English question-and-answer space of BrowseComp-Plus but varies the languages of the supporting documents. XBCP instantiates two complementary settings: in the cross-lingual setting, each query is paired with ev...

4. `2606.07240v1` score=0.2576
   Title: KIT's Submission to Cross-Lingual Voice Cloning in IWSLT 2026
   Categories: cs.CL, cs.SD
   Abstract: Cross-lingual voice cloning aims to generate speech in a target language while preserving speaker identity from a source-language reference. This task is central to speech translation and is the focus of the IWSLT 2026 Cross-Lingual Voice Cloning track. A key challenge is maintaining intelligibility and naturalness in the presence of accent variation and domain-specific vocabulary. We build on a multilingual text-to-speech model, FishAudio-S2-Pro, and introduce language tag prompting to improve language control and reduce accent leakage. We further apply reinforcement learning (RL) fine-tuning for task adaptation and observe improvements in intelligibility. Finally, we propose a reference-co...

5. `2606.16925v1` score=0.2419
   Title: RAID: Semantic Graph Diffusion for True Cold-Start and Cross-Lingual Forecasting
   Categories: cs.AI
   Abstract: Time-series foundation models show strong transfer performance when given a non-empty history window. However, true cold-start scenarios, where a new item has no prior observations, violate this assumption. We propose RAID (Retrieval-Augmented Iterative Diffusion) a framework, which replaces history-based correlation learning with metadata-driven semantic retrieval and graph-conditioned diffusion. RAID maps textual metadata into a shared semantic space using a frozen multilingual embedding model and constructs an inductive retrieval graph that extends naturally to unseen items. It first forms a base forecast by aggregating information from semantically related neighbors, then refines this fo...

6. `2606.08092v1` score=0.2254
   Title: When Languages Disagree: Self-Evolving Multilingual LLM Judges
   Categories: cs.CL
   Abstract: Multilingual LLM-as-a-judge is widely used to evaluate model outputs across languages, but suffers from cross-lingual inconsistency (Fu and Liu, 2025). Existing methods typically treat this inconsistency as noise and mitigate it through voting or aggregation. In this work, we instead show that multilingual inconsistency can provide complementary evaluation signals. Our oracle analysis finds that sampling judgments across languages yields a higher performance upper bound than single-language judging, indicating that different languages potentially include complementary judgments. Motivated by this finding, we propose SEMJ, a self-evolving multilingual judge that leverages cross-lingual incons...

7. `2606.07924v1` score=0.2250
   Title: Decoupling Semantics and Logic: A Training-Free Coarse-to-Fine Pipeline for Video Retrieval-Augmented Generation
   Categories: cs.CV, cs.AI, cs.CL, cs.LG, cs.MM
   Abstract: This paper presents our system description for the 2nd Workshop on Multimodal Augmented Generation via MultimodAl Retrieval (MAGMaR). Addressing the critical challenges of cross-lingual long-video comprehension, strict persona adherence, and zero-hallucination temporal grounding, we propose a fully training-free, two-stage cascaded Video RAG pipeline. Our architecture strategically decouples semantic retrieval from cognitive logical reasoning through a modality-aware division of labor. In the first stage, a high-recall semantic pre-fetching module employs dense retrieval using only high-fidelity visual summaries and global text descriptions, explicitly isolating noisy modalities (e.g., OCR a...

8. `2606.08673v1` score=0.2185
   Title: ClinicalAligner26AM: A Cross-Lingual Aligner for Dataset Translation; Evidences from the MultiClinCorpus Shared Task
   Categories: cs.CL
   Abstract: Word-level cross-lingual alignment is central to annotation projection, translation auditing, and cross-lingual faithfulness estimation, yet existing neural aligners are rarely adapted to specialized domains. In this paper, we introduce ClinicalAligner26AM, a large-context multilingual aligner model for biomedical and clinical text initialized from ClinicalEncoder26AM. Our training recipe is inspired by AWESoME Align. We build our soft alignment target by sharpening with Sinkhorn-Knop optimal transport a cost matrix established for parallel clinical texts and conversations through the fusion of sentence-level, phrase-level, and token-level signals. We distill this sharpened alignment matrix ...


## Candidate 030

Query: low resource machine translation with language models

Likely paper IDs:

1. `2606.11786v1` score=0.4207
   Title: Lius: Translation Model Based Instructional Lingustic Using Continual Instruction Tuning In Kupang Malay
   Categories: cs.CL
   Abstract: Large Language Models (LLMs) offer new potential for translation tasks but often experience performance degradation when handling low-resource languages. To address this limitation, we propose an approach for fine-tuning LLMs on a low-resource language, Kupang Malay. Our approach involves designing a set of instructions by leveraging explicit lexical and semantic features from a bilingual dictionary, and introducing Continual Instruction Tuning (CIT), a training paradigm that enables iterative instruction-based training. Experimental results demonstrate that our model, named Lius, yields notable improvements over standard instruction-tuned models by outperforming 4-6 points, and surpassing b...

2. `2606.16596v1` score=0.2988
   Title: How Far Can Machine Translation Quality Take You? Extrinsic Discourse Evaluation in Goal-Oriented Setups
   Categories: cs.CL
   Abstract: Existing machine translation (MT) metrics and discourse-focused evaluations primarily assess translation quality intrinsically, without measuring the downstream consequences of translation errors. In this work, we focus on extrinsic discourse evaluation of machine translation under two distinct regimes: static and interactive. Under the static regime, we propose an entity counting task as a probe of referential consistency in discourse. We show that high intrinsic MT quality does not reliably predict downstream discourse success and strong MT systems still produce referential inconsistencies. For the interactive regime, we study the goal-oriented multi-agent Welfare Diplomacy game as a probe...

3. `2606.08011v2` score=0.2913
   Title: Rewrite to Translate, Translate to Reward: Reinforcement Learning for Source Rewriting in Machine Translation
   Categories: cs.CL, cs.AI
   Abstract: Rewriting source text with large language models (LLMs) before translation has been shown to improve machine translation (MT) quality. However, we find that prompt-based rewriting can degrade translation quality rather than improve it, particularly when smaller LLMs, such as 4B-parameter models, are used. We argue that this limitation stems from the difficulty of controlling rewriting behavior through natural-language prompts alone: a rewrite is useful only if it improves downstream translation, yet existing prompt-based methods do not explicitly optimize for this signal. To address this issue, we propose RLSR (Reinforcement Learning for Source Rewriting), a reinforcement learning framework ...

4. `2606.13096v1` score=0.2843
   Title: Unified MRI Brain Image Translation via Hierarchical Tumor Structure Comparison
   Categories: cs.CV
   Abstract: Multi-modal MRI brain image translation via available modalities holds significant practical importance in modern medicine, providing robust support for early diagnosis, treatment planning, and outcome assessment of diseases. For this purpose, it is important to ensure the fidelity of the tumor regions after translation. However, existing brain image translation methods ignore the structure information of different tumor regions, which could assist translation models in enhancing the quality and clinical applicability of the translated images. In this work, we propose a novel translation model called HTSCGAN, which is a unified multi-modal brain image translation generative adversarial model...

5. `2606.17354v1` score=0.2822
   Title: Translating the Untranslatable: An Operationalizable Ontology for Untranslatability
   Categories: cs.CL, cs.AI
   Abstract: Untranslatability, cases where meaning cannot be directly preserved across languages, is well-studied in linguistics but underexplored in NLP. As machine translation (MT) systems improve on standard benchmarks, their limitations increasingly concentrate in such cases, where translation cannot be reduced to one-to-one equivalence. We introduce a structured ontology of untranslatability along with a taxonomy of compensation strategies, which are specific techniques to convey meaning under these untranslatable circumstances. We operationalize this framework into a multilingual dataset of untranslatable sentences paired with strategy-based translations, enabling controlled analysis of translatio...

6. `2606.13121v1` score=0.2731
   Title: NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation
   Categories: cs.CL, cs.AI, cs.SD
   Abstract: Simultaneous speech-to-speech translation aims to enable near-real-time communication by minimizing latency, offering a compelling, real-time alternative to the high latency of consecutive translation. However, the excessive pursuit of low latency often results in fragmented chunk-wise speech. Consequently, listeners are subjected to an unnatural acoustic flow punctuated by frequent pauses, which could increase their cognitive load. To bridge this gap, we introduce a fluency-aware optimization framework designed to discover the sweet spot between the low-latency benefits of simultaneous translation and the natural flow of consecutive translation. Our framework minimizes inter-chunk silences ...

7. `2606.20212v1` score=0.2459
   Title: CzechDocs: A Multiway Parallel Dataset of Formatted Documents for Minority Languages in Czechia
   Categories: cs.CL
   Abstract: We present CzechDocs, a multiway parallel dataset of formatted documents (HTML, DOCX, and PDF) covering Czech and minority languages used in Czechia-primarily Ukrainian and English, with smaller portions of Vietnamese, Russian and other languages. The dataset is designed to support the evaluation of machine translation systems that aim to preserve document formatting during translation. We provide a comparison of the most common approaches to format-preserving machine translation on a validation subset of the dataset. This validation split, together with the evaluation toolkit, is publicly released for further research. A held-out test split will be reserved for a future shared task focused ...

8. `2606.08748v1` score=0.2387
   Title: HydraQE: OSU's Submission for the IWSLT 2026 Speech Translation Metrics Shared Task
   Categories: cs.CL
   Abstract: We present HydraQE, our contribution to the IWSLT 2026 Speech Translation Metrics shared task. HydraQE is an end-to-end, reference-free quality estimation (QE) system for speech translation built on a Qwen3-ASR backbone, which accepts source audio and a translation hypothesis as joint input. Hidden states from all backbone layers are combined via a learnable sparsemax scalar mix, then re-encoded by a lightweight bidirectional Transformer to enable full cross-modal interaction prior to pooling into a shared embedding. Three independent prediction heads are trained on complementary supervision signals: human direct assessment (DA) annotations, MetricX-24 pseudo-labels, and xCOMET pseudo-labels...


## Candidate 031

Query: federated learning for foundation models

Likely paper IDs:

1. `2606.16891v1` score=0.4215
   Title: Beyond Weights and Gradients: A Taxonomy of Federated Learning Messages
   Categories: cs.LG, cs.AI
   Abstract: Federated Learning is rapidly evolving beyond the exchange of traditional model weights and gradients, yet existing definitions fail to capture the full scope of modern payloads like synthetic data and federated analytics. This paper addresses the gap by proposing a formal mathematical definition of a federated message that accounts for both utility and privacy. We introduce a taxonomy that organizes these exchanges into three categories: model structures, statistical summaries, and data-conditioned representations. By evaluating these groups based on computational demands, communication costs, and privacy risks, we provide a clearer understanding of the trade-offs involved in decentralized ...

2. `2606.19734v1` score=0.3693
   Title: Federated Bilevel Performative Prediction
   Categories: cs.LG
   Abstract: Federated bilevel optimization is widely used for nested learning problems across distributed clients, such as federated hyperparameter tuning and meta-learning under privacy and communication constraints. Most existing formulations assume fixed client data distributions, which can be violated by performativity, where deployed decisions reshape client behavior and data collection, inducing client-specific, decision-dependent distribution shift. We study federated bilevel performative prediction, where both upper-level (UL) and lower-level (LL) objectives are evaluated under client-dependent, decision-dependent distributions. We formalize the federated bilevel performatively stable (FBPS) poi...

3. `2606.15277v1` score=0.3110
   Title: Guiding Federated Graph Recommendation with LLM-encoded knowledge
   Categories: cs.IR, cs.AI, cs.DB, cs.ET, cs.LG
   Abstract: Graph-based recommender systems are highly effective at extracting collaborative signals from user--item interactions, and federated learning (FL) allows these models to be trained while preserving user privacy. However, aggregating graph representations across distributed, non-IID clients remains a challenge; structural embeddings learned locally often misalign, and naive averaging fails to capture meaningful cross-client relationships. Most existing federated graph methods rely exclusively on structural aggregation, neglecting the rich, global semantic context available in large language models (LLMs). In this paper, we propose a novel framework that uses LLM-encoded knowledge to guide fed...

4. `2606.16868v1` score=0.2918
   Title: Federated Medical Image Segmentation under Real-World Label Noise: A Benchmark Suite for Noisy Label Learning Method Selection
   Categories: cs.CV, cs.AI, cs.DC
   Abstract: While federated learning (FL) enables collaborative medical image segmentation without centralizing sensitive data, real-world deployment is frequently complicated by cross-site label imperfections such as contour disagreement, missing or additional structures, and confused labels. Federated noisy label learning (FNLL) aims to mitigate these effects, yet remains underused in practice as existing evidence is largely based on synthetic noise, simplified settings, and limited real-world noisy evaluation. We address this gap by introducing a benchmark suite that combines diverse real-world noisy datasets, deployment-relevant client-noise scenarios, and label-noise-targeted evaluation to support ...

5. `2606.11556v1` score=0.2907
   Title: Privacy-Preserving Federated Autoencoder for ECG Anomaly Detection on Edge Devices
   Categories: cs.CR, cs.AI, cs.LG
   Abstract: Continuous electrocardiography (ECG) monitoring could surface rhythm abnormalities before they escalate into cardiovascular events. However, a deployable system must satisfy three requirements simultaneously: legal-grade privacy (GDPR, HIPAA), real-time inference on constrained edge hardware, and detection quality under non-IID cross-hospital data. We design and evaluate an end-to-end federated system addressing all three for unsupervised 12-lead ECG anomaly detection on PTB-XL dataset, combining three autoencoder families (VanillaAE, ConvAE, VAE), Flower-based federated averaging (FedAvg) across ten simulated hospitals, client-side differentially private SGD (DP-SGD) with a Rényi-DP account...

6. `2606.08687v1` score=0.2697
   Title: Shift-Dependent Asymmetry: Orthogonal Inverse Low-Rank Adaptation for Federated Medical Segmentation
   Categories: cs.CV
   Abstract: Low-Rank Adaptation (LoRA) enables efficient federated fine-tuning of segmentation foundation models for medical imaging. However, most federated LoRA methods adopt a uniform aggregation rule, which breaks under the encoder-decoder asymmetry in medical segmentation: the encoder is dominated by appearance shifts, while the decoder is dominated by supervision variations. This mismatch entangles shared anatomy with site-specific biases and harms generalization. To address this, we propose Inverse Asymmetric Tuning (IAT). IAT aligns adaptation with heterogeneity sources by personalizing module-specific components in the encoder to absorb appearance shifts and in the decoder to accommodate site-d...

7. `2606.15625v1` score=0.2630
   Title: Conflict-Aware Federated Fine-Tuning of Large Language Models with Mixture-of-Experts
   Categories: cs.LG, cs.NI
   Abstract: The continuous scaling of large language models (LLMs) incurs prohibitive computational costs, making Mixture-of-Experts (MoE) a scalable alternative for efficient fine-tuning via sparse activation. While federated learning (FL) emerges as the paradigm for privacy-preserving collaborative optimization, integrating MoE into FL under data heterogeneity may trigger conflicting expert optimizations. Client-specific data distributions force same-indexed experts to optimize under inconsistent or even conflicting feature-label correlations. This mismatch induces destructive interference during aggregation, thus destabilizing the optimization trajectory and degrading model performance. To address th...

8. `2606.08197v1` score=0.2617
   Title: AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments
   Categories: cs.CL, cs.DC
   Abstract: Large Language Models (LLMs) have significantly propelled the advancement of edge intelligence and have been widely deployed across various scenarios, including autonomous driving, industrial inspection, and personalized IoT services. However, the collaborative adaptation of LLMs on edge devices continues to face formidable challenges due to strict data privacy constraints, highly heterogeneous computing and communication resources, and the non-independent and identically distributed (non-IID) nature of local data. Federated Fine-Tuning (FFT) enables the collaborative optimization of distributed models without exposing raw data. Yet, traditional synchronous aggregation suffers from a severe ...


## Candidate 032

Query: adversarial robustness for vision language models

Likely paper IDs:

1. `2606.08745v1` score=0.2782
   Title: Stain-Aware Wavelet Regularization for Instant Adversarial Purification in Histopathology
   Categories: cs.CV
   Abstract: Deep learning has become prevalent in computational pathology pipelines that support tasks such as cancer screening and digital pathology analysis. However, the susceptibility of neural networks to adversarial perturbations raises safety concerns for reliable deployment in clinical practice. In histopathological images, this challenge is exacerbated by the difficulty of distinguishing high-frequency adversarial noise from subtle and diagnostically relevant tissue structures. To address this issue, we propose Stain-Aware Wavelet Regularization (SAWR), an adversarial purification framework that leverages multi-level wavelet-domain regularization based on Haar transform to hierarchically disent...

2. `2606.10571v1` score=0.2733
   Title: Improving Adversarial Transferability on Vision-Language Pre-training Models via Surrogate-Specific Bias Correction
   Categories: cs.CV, cs.AI, cs.CR
   Abstract: Adversarial examples reveal vulnerabilities in Vision-Language Pre-training (VLP) models and provide insights for improving robustness. A key property is cross-model transferability, which enables transfer-based black-box attacks. However, existing attacks often rely heavily on the surrogate model, causing cross-model performance drops. One reason is that adversarial optimization may follow surrogate model responses more than input semantics, making the update direction effective on the surrogate but less transferable to unseen targets. We refer to this dependency as surrogate-specific bias. Motivated by this observation, DeBias-Attack improves transferability by correcting surrogate-specifi...

3. `2606.17482v1` score=0.2639
   Title: SPHINX: First Explain, Then Explore
   Categories: cs.CV
   Abstract: Generating adversarial driving scenarios is critical for evaluating and improving autonomous vehicle decision-making systems in simulation. Recent approaches, such as ChatScene and LLM-Attacker, rely primarily on the prior knowledge of Large Language Models and Vision-Language Models to generate driving scenarios procedurally. We argue that adversarial scenes should be generated based on the failure diagnosis (e.g., indecisiveness, multi-frame inconsistency) of the driving policy to specifically address the policy's weaknesses instead of relying on prior assumptions. In this paper, we propose SPHINX, a closed-loop framework for adversarial scenario synthesis guided by a simple principle: fir...

4. `2606.11906v1` score=0.2597
   Title: When Does Language Matter? Multilingual Instructions Reveal Step-wise Language Sensitivity in Vision-Language-Action Models
   Categories: cs.CL
   Abstract: Vision-Language-Action (VLA) models have shown strong performance in language-conditioned robotic manipulation, yet their robustness to linguistic variation remains poorly understood. In this work, we present the first systematic multilingual evaluation of VLA models by translating the LIBERO benchmark into ten languages, revealing severe performance degradation under non-English instructions, with success rates dropping by 30-50%. Through fine-grained analysis of task executions, we find that language influence is highly non-uniform across steps: certain steps exhibit strong language dependence and dominate overall task failure, while others are largely language-agnostic. Based on this insi...

5. `2606.19584v1` score=0.2492
   Title: Language-Instructed Vision Embeddings for Controllable and Generalizable Perception
   Categories: cs.CV
   Abstract: Vision foundation models are typically trained as static feature extractors, placing the burden of task adaptation onto large downstream models. We propose an alternative paradigm: instead of solely feeding visual features into language models, we use language itself to dynamically guide the vision encoder. Our method, Language-Instructed Vision Embeddings (LIVE), leverages language as high-level guidance to produce task-centric embeddings at inference time, removing the need for task-specific retraining. This enables the encoder to focus on contextually relevant aspects of the input, yielding more controllable and generalizable representations. Empirically, LIVE reduces visual hallucination...

6. `2606.12075v1` score=0.2465
   Title: Categorical Robustness Assessment for Machine Learning based Network Intrusion Detection Systems
   Categories: cs.CR, cs.LG
   Abstract: Network Intrusion Detection Systems (NIDS) heavily utlize Machine Learning (ML) but ML models can be manipulated via adversarial attacks. These attacks add carefully crafted perturbations to network traffic data that leads to misclassifications. While prior work has demonstrated adversarial vulnerabilities in isolated settings, systematic cross-architecture as well as class and category of attack based comparisons under controlled attack conditions remain limited, leaving practitioners without clear guidance on which models to deploy in adversarial environments. This paper asks a simple question: what type of classifier architectures actually hold up when attackers try to manipulate the syst...

7. `2606.11409v1` score=0.2219
   Title: Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models
   Categories: cs.LG, cs.AI, cs.CR
   Abstract: Adversarial robustness evaluations of large language models (LLMs) typically report attack success rate (ASR) under fixed query budgets, implicitly treating all attacks as equally costly. In practice, the computational expense of different attack strategies can vary by orders of magnitude. Consequently, ASR at a fixed budget can obscure the true effort required to jailbreak a model, thereby making it hard to determine whether an attack's cost justifies its payoff to the attacker. We propose a compute-aware evaluation framework based on computational pressure, measured in cumulative floating-point operations (FLOPs), as a proxy for adversarial effort. We introduce risk-compute curves, which m...

8. `2606.07696v1` score=0.2189
   Title: Adversarial Robustness of Activation Steering in Large Language Models
   Categories: cs.LG, cs.AI
   Abstract: Activation steering has become a popular training-free method to control LLM behavior by injecting precomputed direction vectors into the model's residual stream at inference time. Yet its robustness to realistic input variation remains unstudied. We present the first systematic evaluation of activation steering robustness under adversarial text perturbations on the inputs, covering four extraction methods, three attack strategies, six personas from Anthropic Model-Written Evaluation Dataset, and five models ranging from 1.5B to 30B parameters. Attacks succeed broadly across all settings: directional robustness drops by up to 64%, post-attack confidence collapses near or below 0.25 across al...


## Candidate 033

Query: explainability for deep learning models

Likely paper IDs:

1. `2606.09568v1` score=0.2619
   Title: Self-Explainability in Self-Adaptive and Self-Organising Systems: Status and Research Directions
   Categories: cs.AI
   Abstract: The growing complexity of self-adaptive and self-organising systems, fuelled by advances in Artificial Intelligence (AI), has made them increasingly difficult to understand and trust. While Explainable AI aims to provide insight into AI decision-making, a more advanced goal is for systems to explain themselves - an ability referred to as Self-Explainability (SX). This article presents a systematic literature review on SX, analysing existing approaches, including their domains, targets, and evaluation methods. The review develops a unified definition and taxonomy of SX and introduces Levels of Self-Explainability, providing a framework for positioning current and future research. Our results ...

2. `2606.10170v1` score=0.2370
   Title: Learning Entropy and Spatial Adaptation Dynamics of Multilayer Perceptrons for Structural Point Extraction
   Categories: cs.LG
   Abstract: This paper extends the concept of Learning Entropy (LE) from temporal adaptive systems to spatial learning in multilayer perceptron networks (MLPs) applied to image data. Instead of evaluating image structure directly from gradients or covariance operators, as local neighborhood methods do, the proposed approach analyzes the learning process itself through Learning Entropy. An MLP is trained to predict the intensity of a center pixel from its surrounding spatial context, while LE is evaluated from the incremental adaptation of neural weights during learning across image-derived samples. The resulting Spatial Learning Entropy Maps (SLEM) identify unusual image points and regions that induce s...

3. `2606.20299v1` score=0.1926
   Title: Statistical Properties of Training & Generalization
   Categories: stat.ML, cs.LG, hep-ph, physics.data-an
   Abstract: Deep learning has managed to evade numerous intuitions from classical statistics to achieve unprecedented performance on a number of real-world tasks. In this article, we investigate the key features and surprises of deep learning from a physics-informed perspective, taking care to point out and justify where possible the many choices inherent in constructing a deep learning model. In particular, we review the phenomenon of neural scaling laws and discuss their interplay with the constraints and inductive biases which may be present when applying machine learning to problems in physics.

4. `2606.20108v1` score=0.1926
   Title: EFIQA: Explainable Fundus Image Quality Assessment via Anatomical Priors
   Categories: cs.CV, cs.LG
   Abstract: Image quality control is vital for a wide range of downstream applications. Deep learning-based image quality assessment methods typically train classifiers on dataset-specific quality labels, inheriting two limitations: (1) generalization is tied to the labeling criteria of the training set and (2) these methods cannot provide spatial feedback on where the quality is degraded, lacking explainability. In this work, we propose EFIQA, a framework that requires no quality-related supervision and produces spatial quality maps by design. Rather than learning ``what is degradation" from human-annotated labels, EFIQA learns ``what should be there" by leveraging anatomical priors. For fundus photogr...

5. `2606.07503v1` score=0.1916
   Title: Differences in Detection: Explainability Where it Matters
   Categories: cs.CV
   Abstract: We propose Differences in Detection (DnD), an intuitive method to compare two object detection models. Based on the same matching algorithm, it complements the standard metrics of mean Average Precision ($mAP$) and TIDE error analysis with the ability to compare two models directly. More specifically, we calculate the intersection of ground truth labels that are recognized by both models, followed by the corresponding difference sets and the complement set of ground truth labels that are missed by both models. The resulting comparison is more direct and intuitive than a comparison of independent summary statistics. It reveals individual and shared mistakes and becomes particularly interestin...

6. `2606.19920v1` score=0.1758
   Title: Deep-Unfolded Coordination
   Categories: cs.RO, cs.LG, cs.MA
   Abstract: Distributed optimization is a highly scalable and structurally transparent technique to solve multi-agent robotics problems; however, such methods often suffer from the need for highly-specialized, problem-specific hyperparameter tunings. In this work, we propose Deep Coordinator, a deep-unfolding framework that learns to dynamically adjust the hyperparameters of ADMM-DDP, a popular distributed solver for robotics tasks, at solve-time in response to optimizer performance. Our architecture consists of unrolling a fixed number of ADMM-DDP iterations into a neural network with learnable functions between layers mapping the optimizer state to the next hyperparameters. To the best of our knowledg...

7. `2606.08806v1` score=0.1741
   Title: Governance Controls for AI-Generated Test Artifacts in Autonomous Software Testing
   Categories: cs.SE, cs.AI
   Abstract: Artificial Intelligence (AI) and Large Language Models (LLMs) are increasingly used in autonomous software testing; however, AI-generated test artifacts often suffer from hallucinations, compliance violations, security risks, and limited explainability. To enhance the reliability, transparency, and trustworthiness of AI-generated testing artifacts, this research introduces the concept of Governance-Aware Autonomous Testing Framework (GATF). The framework extends the autonomous testing lifecycle with governance validation, explainability analysis, probabilistic risk assessment, compliance monitoring, as well as audit governance. Experiments were performed with Defects4J and PROMISE software e...

8. `2606.12252v1` score=0.1717
   Title: Using Explainability as a Training-Time Reliability Signal for Efficient ECG Classification
   Categories: cs.LG, cs.AI
   Abstract: Training deep neural networks for clinical time-series analysis is computationally demanding, yet many healthcare settings lack the resources required for repeated model development and deployment. This challenge is particularly evident in electrocardiogram classification, where large datasets and long training schedules make efficiency practically important. Progressive Data Dropout reduces training cost by excluding samples from gradient updates once they are learned, but it relies on model confidence and may retain samples that are difficult due to noise or ambiguity rather than useful signal. In this work, we introduce ERTS, an explainability-based reliability training signal for efficie...


## Candidate 034

Query: causal reasoning in machine learning

Likely paper IDs:

1. `2606.11745v1` score=0.4880
   Title: From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning
   Categories: cs.CV, cs.AI
   Abstract: Visual causal reasoning is essential for understanding and intervening in the physical world, requiring identification of causal variables from visual inputs and reasoning over intervention effects. Despite recent progress, large vision--language models (VLMs) remain brittle at such tasks, especially for interventional and counterfactual queries over multi-image inputs. Most existing explorations inject causal knowledge via textual prompts, leaving causal mechanisms external to model execution and limiting reliable control during inference. To address this problem, we propose BridgeVLM, which internalizes visual causal reasoning by inducing a causal graph from multi-image inputs and converti...

2. `2606.10607v1` score=0.4046
   Title: Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: Causal discovery aims to uncover causal structures from observational data, which is crucial for real-world decision-making. However, different causal discovery algorithms can produce divergent results that conflict with each other, complicating the identification of accurate causal graphs. Traditional approaches rely on numerical values and statistical assumptions, often ignoring rich domain-specific information, such as feature descriptions, which could also help structure learning. While recent works explore using Large Language Models (LLMs) to infer causal relations via direct queries, such methods can be unreliable due to a lack of alignment with the actual data. To address these limit...

3. `2606.09181v1` score=0.3660
   Title: Counterfactual Reasoning for Fine-Grained Evidence Disentanglement in VideoQA
   Categories: cs.CV, cs.LG
   Abstract: Recent advances in video multimodal models have significantly improved VideoQA performance. However, these systems often rely on spurious statistical correlations rather than answer-relevant causal evidence, resulting in unfaithful and brittle reasoning, especially in complex real-world scenarios. Existing methods either rely on cross-modality correlations, costly curated training resources, or insufficient causal assumptions and constraints, and typically operate at the time-interval level. As a result, they fail to explicitly disentangle causal visual cues from confounders and provide limited fine-grained evidence localization. To address this issue, we propose a Counterfactual Reasoning f...

4. `2606.11470v1` score=0.3426
   Title: The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes
   Categories: cs.CL
   Abstract: Large Language Models (LLMs) have achieved strong performance across natural language processing tasks, yet reliable reasoning remains an open challenge. Although modern LLMs show progress in structured inference, multi-step problem solving, and contextual understanding, their reasoning behavior is often inconsistent and sensitive to prompting strategies, task design, and model scale. This survey provides a systematic analysis of more than 300 recent papers from arXiv, Semantic Scholar, Google Scholar, Papers with Code, and the ACL Anthology to examine how reasoning capabilities emerge in LLMs and where they fail. We make three main contributions. First, we introduce a structured taxonomy of...

5. `2606.14892v1` score=0.3404
   Title: Relational Structural Causal Models
   Categories: cs.AI, cs.LG, cs.SI, stat.ML
   Abstract: An artificial intelligence must have a model of its environment that is causal, supporting reasoning about interventions and counterfactuals, and also combinatorial, supporting generalization to unseen combinations of objects. In this work, we formally study when and how such a model can be learned. We develop relational structural causal models, extending structural causal models (Pearl 2009) to settings where objects and their relations vary. First, we show how answers to not only causal but also observational queries about unseen combinations of objects can not be identified without further assumptions. To enable such identification--including in the presence of unobserved confounding--we...

6. `2606.15756v1` score=0.3072
   Title: From Correlation to Causation in Lane Change Prediction for Automated Driving: A Causal Explanation Framework
   Categories: cs.LG, cs.AI
   Abstract: Lane-change prediction is a central task in intelligent vehicles, where early maneuver anticipation can support safer decision-making. However, many existing approaches mainly learn statistical associations between observed driving variables and future maneuvers, while overlooking the causal dependencies among the input variables themselves. This limits interpretability, especially when physically related variables such as longitudinal gap, relative longitudinal velocity, and Time-To-Collision (TTC) are treated as independent flat inputs. This article presents a causal-inference-based framework for lane-change prediction and explanation. The proposed approach combines linguistic feature cons...

7. `2606.17516v1` score=0.2982
   Title: FoundCause: Causal Discovery with Latent Confounders from Observational Data
   Categories: cs.LG, cs.AI, stat.ME, stat.ML
   Abstract: Causal discovery from observational data remains challenging due to the need to recover directed structure and latent confounding without interventions. We propose FoundCause, an amortized causal discovery model trained entirely on synthetic data that maps datasets directly to causal graphs in a single forward pass. By learning from large collections of simulated structural causal models, FoundCause captures transferable statistical patterns that generalize beyond individual datasets. The architecture incorporates several key inductive biases for causal discovery. It uses a permutation-invariant transformer encoder with alternating attention over samples and variables to jointly model cross-...

8. `2606.09957v1` score=0.2839
   Title: Data-aware Static Analysis: Improving Detection of Semantic Faults in Machine Learning Code Using Data Characteristics
   Categories: cs.SE, cs.LG
   Abstract: Semantic faults specific to the use of machine learning models are a common problem for machine learning developers, causing suboptimal predictions, high computational cost, or incorrect outputs. For example, one may erroneously use unscaled data to train a scale-sensitive model. Machine learning developers detect these faults after training their models and manually analyzing the results, making it an inefficient process. We propose a novel data-aware static analysis approach to detect semantic faults in machine learning code, allowing developers to reveal these bugs while writing code instead of after training the model. Our approach uses combined data and control flow analysis, and API co...


## Candidate 035

Query: reinforcement learning from human feedback

Likely paper IDs:

1. `2606.20482v1` score=0.3024
   Title: Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users
   Categories: cs.CL, cs.HC, cs.LG
   Abstract: To align a Large Language Model (LLM), most existing methods collect explicit human feedback and train a reward model to predict the human preference based on the response text. These existing methods have two key limitations. First, the users rarely provide explicit feedback for LLM responses, which makes the high-quality preference annotation expensive to collect. Second, the methods do not leverage implicit human feedback, which has proven vital to the economic moats of Internet giants. To quantify the value of implicit feedback, we build a new dataset called IFLLM, which collects 1336 multi-turn questions from the 59 Mechanical Turk workers, their mouse trajectories, and eye gazing point...

2. `2606.14368v1` score=0.2916
   Title: Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback
   Categories: cs.LG, cs.CL
   Abstract: We study multi-domain LLM training in which two models, each stronger in a different domain, co-evolve by tutoring each other through on-policy feedback. Unlike one-way distillation or single-model fine-tuning, our goal is mutual Pareto improvement: each model improves across domains without losing its original strength. To this end, we propose On-Policy Co-Distillation (OPCoD), where each student's self-distillation is conditioned on its own correct rollout and feedback from its peer. To make feedback exchange effective, OPCoD uses cognizance-based gating to decide when to give feedback and feedback anchoring to ground feedback in the problem. On Science Q\&A tasks, OPCoD consistently outpe...

3. `2606.09124v1` score=0.2814
   Title: A Regret Minimization Framework on Preference Learning in Large Language Models
   Categories: cs.AI
   Abstract: Reinforcement learning with verifiable rewards (RLVR) has enabled progress on reasoning-intensive tasks by relying on task-specific verifiers that provide automated correctness signals. However, many realistic language tasks are difficult to equip with reliable verifiers, motivating a growing reliance on reinforcement learning from human feedback (RLHF). In this setting, we argue that a closer examination of how human feedback should be interpreted is essential. We introduce Regret-based Preference Optimization $(\textbf{RePO})$, which reframes RLHF through $\textit{regret minimization}$ rather than reward maximization. Human preferences are often shaped by $\textit{prospective}$ anticipatio...

4. `2606.20287v1` score=0.2563
   Title: PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback
   Categories: cs.CL
   Abstract: Effective Automated Essay Scoring (AES) are expected to support both reliable assessment and actionable instructional feedback. However, existing approaches often treat scoring and feedback as separate components: neural scoring models provide limited interpretability, while Large Language Model (LLM)-based feedback is typically insensitive to learners proficiency levels. To address this fragmentation, this work proposes PsyScore, a psychometrically-aware framework that integrates diagnostic assessment with instructional scaffolding through a shared latent ability representation. PsyScore comprises three key modules: a Trait-Adaptive Neural IRT Scorer that incorporates the Graded Partial Cre...

5. `2606.18591v1` score=0.2404
   Title: Bridging Creative Intent and Visual Quality: Creator-Driven Recurrent Video Generation with Agentic Feedback Loops
   Categories: cs.CV
   Abstract: Generative AI has made content creation increasingly accessible, but many AI-generated videos lack narrative coherence and creative direction, issues that become more substantial at longer durations. Unlike coding, where AI generation benefits from reliable feedback and techniques such as recurrent self-improvement, video generation requires subjective feedback about plot, scenes, and narrative, which naturally motivates approaches that incorporate human creative direction. We introduce CHIEF, a human-AI co-creation video generation framework that places the creator at the center of human-in-the-loop iterative video refinement, and supports them by providing automatic subjective feedback. Th...

6. `2606.13604v1` score=0.2320
   Title: Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch
   Categories: cs.AI, cs.LG, cs.MA
   Abstract: Dispatch in three-sided marketplaces provides a natural setting for reinforcement learning from world feedback: decisions are evaluated by delayed operational outcomes such as delivery speed, courier utilization, and merchant congestion. We present a deployed reinforcement learning system at DoorDash that adapts dispatch objective weights in a large-scale food-delivery marketplace using delayed signals. Rather than replacing the combinatorial assignment optimizer, a store-level policy learned from logged marketplace data selects a discrete multiplier that shifts the dispatch optimizer's tradeoff between delivery quality and batching efficiency. This interface enables offline policy learning ...

7. `2606.20068v1` score=0.2269
   Title: Process-Verified Reinforcement Learning for Theorem Proving via Lean
   Categories: cs.AI
   Abstract: While reinforcement learning from verifiable rewards (RLVR) typically has relied on a single binary verification signal, symbolic proof assistants in formal reasoning offer rich, fine-grained structured feedback. This gap between structured processes and unstructured rewards highlights the importance of feedback that is both dense and sound. In this work, we demonstrate that the Lean proof assistant itself can serve as a symbolic process oracle, supplying both outcome-level and fine-grained tactic-level verified feedback during training. Proof attempts are parsed into tactic sequences, and Lean's elaboration marks both locally sound steps and the earliest failing step, yielding dense, verifi...

8. `2606.19370v1` score=0.2228
   Title: Human-like autonomy emerges from self-play and a pinch of human data
   Categories: cs.LG, cs.AI, cs.MA
   Abstract: Self-play reinforcement learning has recently emerged as a way to train driving policies without any human data. It uses cheap, large-scale simulations to substitute expensive, large-scale human driving demonstrations. A key limitation of this approach is that policies trained through pure self-play can learn effective but alien driving conventions incompatible with people. Previous works attempt to mitigate such behavioral misalignments through extensive reward engineering and domain randomization, which are brittle and labor-intensive. Instead of completely discarding human demonstrations, our method treats them as a regularization objective on top of a minimal safe goal-reaching reward. L...


## Candidate 036

Query: automatic evaluation of generated summaries

Likely paper IDs:

1. `2606.10142v1` score=0.1733
   Title: DB-3DME: From Dataset to Benchmark for Human-aligned Automatic 3D Mesh Evaluation
   Categories: cs.CV
   Abstract: Recent advances in 3D generation have led to substantial improvements in realism, controllability, and efficiency, yet the evaluation of 3D assets remains underexplored. Existing evaluation paradigms, including human evaluation, learned metrics, and vision-language models (VLMs) as judges, suffer from limitations in cost, scalability, resolution handling, or task-specific alignment. In this work, we focus on 3D mesh evaluation and introduce DB-3DME, the Dataset and Benchmark for 3D Mesh Evaluation. DB-3DME contains 2,619 synthetic 3D meshes paired with human ratings on Geometry and Prompt Adherence. Using this dataset, we systematically benchmark state-of-the-art VLMs and identify visual enc...

2. `2606.08000v1` score=0.1724
   Title: Summarization is Not Dead Yet
   Categories: cs.CL, cs.AI
   Abstract: The progress of large language models (LLMs) has fueled claims that model-generated summaries rival or even surpass human-written references, raising questions about whether summarization remains an open research problem. We re-examine this narrative through a multi-track evaluation covering five diverse datasets and five state-of-the-art LLMs, combining controlled human assessment, bias-mitigated LLM-as-Judge protocols, factuality verification against external knowledge, and corpus-level linguistic analysis. Our findings reveal a more nuanced landscape in which human reference summaries continue to demonstrate advantages in informativeness and faithfulness, whereas LLM outputs are preferred...

3. `2606.15735v2` score=0.1722
   Title: EHRNote-ChatQA: A Benchmark for Evidence-Grounded Multi-Turn Clinical Question Answering over Longitudinal Discharge Summaries
   Categories: cs.CL, cs.AI
   Abstract: Discharge summaries are crucial clinical documents containing the context of a patient's overall hospital stay, and are routinely reviewed by medical experts for patient readmission, ongoing care, and diagnostic decision-making. When reviewing them, medical experts often must iteratively synthesize information across multiple summaries while verifying the evidence supporting each answer. Although large language models (LLMs) are increasingly explored for clinical question answering, existing benchmarks do not sufficiently reflect this setting: they often evaluate exam-style medical knowledge or focus on single-turn question answering with limited evidence-grounding evaluation. We introduce E...

4. `2606.10833v1` score=0.1162
   Title: Do VLMs Reason Like Engineers? A Benchmark and a Stage-wise Evaluation
   Categories: cs.AI
   Abstract: Vision-Language Models (VLMs) demonstrate strong performance on general multimodal reasoning benchmarks, yet their ability to perform engineering reasoning remains largely unexplored. Unlike general visual question answering, engineering problem solving requires interpreting technical diagrams, selecting governing physical principles, and maintaining physically consistent multi-step reasoning. These capabilities are increasingly important for AI systems used in engineering education, scientific assistance, and technical decision-making, where reasoning failures may produce physically invalid yet superficially plausible solutions. Existing benchmarks primarily evaluate final answers and provi...

5. `2606.11738v1` score=0.1160
   Title: Renewable Lasso without Batch-Number Constraints: A Gradient-Enhanced Approach
   Categories: stat.ML, cs.LG
   Abstract: We study online estimation for high-dimensional generalized linear models with streaming data. First, for the non-distributed setting, we propose a gradient-enhanced surrogate loss that approximates the cumulative loss using only historical summaries, which modifies and improves upon the existing renewable estimation approach for the same model in the high-dimensional setting, and removes the batch-number constraint in previous studies. We then extend the method to distributed streaming data under the master-client architecture, where batches are partitioned across sites and only summaries (gradient vectors) are exchanged. Instead of directing applying the popular method of Jordan et al. (20...

6. `2606.14516v1` score=0.1144
   Title: Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results
   Categories: cs.AI, cs.CL, cs.CY
   Abstract: AI evaluations are widely used for testing and understanding progress. However, the diverse evaluators bring with them inconsistencies that challenge analysis and comparison. First, results are saved in incompatible formats, scattered across leaderboards, papers, blog posts, evaluation harness logs, and custom repositories. Second, results are created by different evaluation frameworks, which produce divergent scores for nominally identical evaluations and record metadata inconsistently, hindering comparison, cross-community evaluation science, cost reduction, and reuse. We introduce Every Eval Ever, the first shared schema and community-crowdsourced repository for AI evaluation results. The...

7. `2606.08445v1` score=0.1132
   Title: Segment-level Tree Search for Long Meeting Document Summarization
   Categories: cs.CL, cs.AI
   Abstract: Meeting documents are challenging to summarize due to their length and complex conversational structure. Existing approaches typically adopt multi-stage pipelines that extract information prior to summarization; however, these approaches often suffer from cumulative error propagation without intermediate validation, a limitation further amplified by short and low-quality reference summaries. We propose segment-level summarization via Monte Carlo Tree Search (S3), a training-free framework that constructs a final summary by composing segment-level summary candidates. S3 partitions a long document into segments and generates multiple summary candidates per segment, forming nodes of a search tr...

8. `2606.16015v1` score=0.1101
   Title: Stringalign: Moving beyond summary statistics with a transparent Unicode-aware tool for evaluating automatic transcription models
   Categories: cs.CV
   Abstract: Comparing text strings is crucial when evaluating and understanding the performance of various text processing tasks such as document recognition and audio transcription. With an increasingly complex landscape of AI-based handwritten text recognition (HTR), optical character recognition (OCR) and automatic speech recognition (ASR) models, there is a need for tools that facilitate evaluation in a flexible and reproducible way. This paper presents Stringalign, a Python library designed to simplify the evaluation process for automatic transcription projects and facilitate transparent evaluation. Stringalign's tools to examine and visualise both the rate of errors and the types of errors a model...


## Candidate 037

Query: document question answering with retrieval

Likely paper IDs:

1. `2606.10921v1` score=0.4183
   Title: Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering
   Categories: cs.CL
   Abstract: Long-document question answering (QA) requires large language models (LLMs) to reason over evidence scattered across lengthy documents, where answers often depend on event order, section-level context, and cross-part evidence connections. Although retrieval-augmented generation (RAG) reduces the input context by retrieving relevant evidence, existing structured RAG methods still face three limitations: costly query-agnostic knowledge organization, insufficient use of original document structure, and no reuse of historical reasoning experience. To address these limitations, we propose DocTrace, a multi-agent RAG framework for long-document QA that supports query-triggered knowledge organizati...

2. `2606.18781v1` score=0.4117
   Title: Lost in a Single Vector: Improving Long-Document Retrieval with Chunk Evidence Aggregation
   Categories: cs.CL
   Abstract: Dense retrieval ranks one query vector against one document vector. On long documents, this interface can fail when a short but decisive span is weakened during document encoding before ranking. We study this failure mode as document-side early compression and introduce the Evidence Dilution Index (EDI) to measure how far a document-level representation falls below the strongest chunk-level evidence within the same gold document. Guided by this view, we propose DICE (Document Inference via Chunk Evidence), a training-free document-side strategy that splits documents into chunks, encodes them independently with a frozen model, and aggregates them back into a single vector while preserving the...

3. `2606.10381v1` score=0.2704
   Title: Agentic Hybrid RAG for Evidence-Grounded Muon Collider Analysis
   Categories: hep-ex, cs.AI, cs.CL, cs.IR, physics.ins-det
   Abstract: Muon collider research spans accelerator physics, detector instrumentation, and high-energy phenomenology, with relevant evidence scattered across a rapidly expanding and heterogeneous body of scientific literature. As high-energy physics (HEP) increasingly explores agent-assisted analysis workflows, efficiently locating, integrating, and verifying scientific evidence becomes an essential capability. While retrieval-augmented generation (RAG) offers a promising framework for scientific question answering, integrating agentic reasoning without compromising retrieval precision remains a key challenge. In this work, we present agentic hybrid RAG, an evidence-grounded RAG framework for muon coll...

4. `2606.11613v1` score=0.2657
   Title: Factions Within, Uncertain Across: Within-Document Reader Sub-Groups in Social Highlighting
   Categories: cs.IR, cs.CL, cs.HC, cs.SI
   Abstract: When many people highlight the same document, is the crowd a single consensus, or is it internally structured into reader sub-groups that mark different things -- and is that structure a stable property of a reader or of the document? Building on prior work showing an individual's within-document highlighting signal is a whisper while individuality lives in selection, we ask the group-level question on a co-readership platform using a margin-preserving curveball null. Experiment 1: within a document, readers form strong sub-groups -- pairs agree far beyond what shared salience, mark density, and sentence popularity predict (nearest-neighbour agreement z=+6.3, significant in 88% of documents)...

5. `2606.11945v1` score=0.2375
   Title: uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking
   Categories: cs.CL, cs.IR
   Abstract: This report describes our participation in SemEval-2026 Task 8 on multi-turn retrieval and question answering. The task evaluates conversational systems across four domains (finance, cloud documentation, government, Wikipedia), and includes unanswerable queries where the available collection does not contain sufficient evidence to produce a complete response. We propose a multi-turn retrieval-augmented generation pipeline that combines learned sparse retrieval with LLM-based reranking and generation. Using sparse retrieval as the primary retrieval method, we leverage its strong generalization across domains. In addition, we make use of the long-context capabilities of LLMs for conversational...

6. `2606.09459v1` score=0.2254
   Title: AbstRAG: Learning to Abstract for Retrieval Problems
   Categories: cs.CL
   Abstract: Retrieval-augmented generation often fails when the query, the document evidence, and the user's intent are expressed at different levels of abstraction. A query may ask about a class, a relation, or an event, while the document only states specific instances, indirect framings, or scoped formulations. We define this mismatch as an abstraction gap: the minimal set of typed assumptions required to align query intent with the available evidence. To close this gap, we introduce AbstRAG, which treats abstraction as an explicit retrieval object. AbstRAG decomposes the query--evidence gap into expression, conceptual, intent--evidence, and event-type components, and scores relevance by combining ma...

7. `2606.19759v1` score=0.2130
   Title: Optimal Scheduling in a Question-Answering Forum of Knowledge Workers
   Categories: cs.AI, cs.SI
   Abstract: As individuals turn to the Internet to find answers to questions they may have, several Question Answering (QA) forums have evolved, where users knowledgeable in certain topics can contribute their expertise to answering these requests for information. While these are currently volunteer based, we consider a future version employing knowledge workers who are experts in certain topics. In such a system, the request-answer processes forming the queuing system may utilize schedulers that assign requests in different topics to the experts in the forum, who may be able to answer them according to their expertise levels in different topics. With this model, we calculate the capacity of the system ...

8. `2606.15861v1` score=0.2117
   Title: Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
   Categories: cs.CV
   Abstract: Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, with the potential to support surgical training and intraoperative decision-making. Recent Vision-Language Models (VLMs) have shown promising performance through parameter-efficient fine-tuning; however, most existing approaches rely on coarse visual grounding, typically limited to bounding boxes, which fails to capture the fine-grained spatial structure of surgical objects. In this work, we propose a unified framework that jointly performs pixel-level segmentation and visual question an...


## Candidate 038

Query: knowledge graph augmented language models

Likely paper IDs:

1. `2606.11560v1` score=0.4119
   Title: LLMs+Graphs: Toward Graph-Native, Synergistic AI Systems
   Categories: cs.DB, cs.AI
   Abstract: Large Language Models (LLMs) have advanced rapidly, but their limitations in structured and multi-hop reasoning underscore the need for graph-native, synergistic artificial intelligence (AI) systems. Graph-structured data underpins critical applications across social, biological, financial, transportation, web, and knowledge domains, making it essential to understand how LLMs can leverage graph computation for grounded, context-rich inference. Three complementary synergies are emerging: LLMs augmented with graph computation for retrieval and reasoning; bidirectional integration between LLMs and knowledge graphs (KGs), where LLMs support KG construction and curation while KGs enforce semantic...

2. `2606.10875v1` score=0.3846
   Title: Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation
   Categories: cs.CL
   Abstract: Large language models (LLMs) rely on tool use to act as autonomous agents, yet often fail in multi-step execution due to insufficient tool-related knowledge and ineffective knowledge activation. Therefore, we present a systematic study on how knowledge influences tool-use performance, covering the stages of knowledge acquisition, activation, and internalization. In the knowledge acquisition stage, we acquire and evaluate various forms of experiential knowledge, and our analysis shows that simple instance-level knowledge can already provide strong and reliable gains, while abstract intent-level knowledge offers limited benefits. At inference time, to activate knowledge, we find that prompting...

3. `2606.16509v1` score=0.3774
   Title: Model Graph Inductive Learning for Knowledge Graph Completion
   Categories: cs.AI
   Abstract: Link prediction in knowledge graphs fundamentally depends on the quality of learned embeddings for entities and relations. However, most existing methods derive these embeddings by aggregating only the local neighborhood of each entity, neglecting the global structure of the knowledge graph. This limited view prevents models from capturing higher-level structural patterns that are essential for accurate and generalizable link prediction. To address these limitations, we introduce Model Graph Inductive Learning (\textbf{MGIL}), a framework that constructs a model graph by clustering entities based on the similarity of their incoming and outgoing relational structures or their entity types. A ...

4. `2606.17667v1` score=0.3653
   Title: Handling Feature Heterogeneity with Learnable Graph Patches
   Categories: cs.LG, cs.AI
   Abstract: In recent years, the rapid development of foundation models and graph pre-training technologies has spurred increasing interest in constructing a universal pre-trained graph model or Graph Foundation Model (GFM). However, a significant challenge is that existing models are unable to address feature heterogeneity in graph data without textual information, which hinders the transferability of graph models across different datasets. To bridge this gap, we propose the concept of learnable graph patches, which we regard as the smallest semantic units of any graph data. We decompose the graph into learnable graph patches by unfolding the node features and constructing corresponding patch structure...

5. `2606.12687v1` score=0.3201
   Title: Forecasting Is Not Attribution: Localizing Decoder Bypass in Graph-Based Neural Marketing Mix Models
   Categories: cs.LG
   Abstract: Marketing mix models are used to forecast business outcomes and to attribute those outcomes to marketing channels, but these goals are not equivalent. We study a failure mode in graph-based neural MMM called attribution bypass: a high-capacity decoder can obtain low forecasting error through target autoregression, dense communication, co-movement, context, or latent memory while failing to route counterfactual sensitivity through the graph used as the attribution object. We introduce DICE-MMM as a bounded diagnostic and training framework. We do not claim that observational neural MMM identifies causal effects. Instead, DICE separates three questions often conflated in graph-based MMM: graph...

6. `2606.14047v1` score=0.3150
   Title: Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling
   Categories: cs.IR, cs.AI, cs.CL, cs.LG
   Abstract: Long-context language modeling requires not only extending context windows but maintaining coherent understanding of entity states and relationships across thousands of tokens -- a challenge that semantic similarity alone cannot address. KGERMAR addresses this by constructing dynamic, context-specific knowledge graphs from input text during inference, enabling domain-adaptive retrieval that leverages both semantic similarity and explicit entity relationships. The framework performs real-time entity and relation extraction to build contextual knowledge graphs, then integrates graph-structural embeddings with textual semantics through a multi-component memory architecture. Three memory banks -...

7. `2606.09105v3` score=0.2787
   Title: Graph2Idea:Retrieval-Augmented Scientific Idea Generation with Graph-Structured Contexts
   Categories: cs.AI
   Abstract: Generating novel, feasible, and high-quality research ideas is an important yet challenging task in scientific discovery. Recent Large Language Model (LLM)-based methods often ground idea generation with retrieved literature, but the retrieved evidence is usually provided as flat text, such as titles, abstracts, or summaries. Such flat contexts may contain redundant or weakly relevant information, while making cross-paper relations among problems, methods, mechanisms, and findings difficult to identify and trace. To address this challenge, we propose Graph2Idea, a knowledge graph-guided framework for retrieval-augmented scientific idea generation.Graph2Idea first retrieves papers according t...

8. `2606.14243v1` score=0.2673
   Title: Decoupled Mixture-of-Experts for Parametric Knowledge Injection
   Categories: cs.CL
   Abstract: Knowledge injection aims to equip large language models (LLMs) with external, domain-specific, or time-sensitive knowledge. Existing approaches typically face a trade-off between flexibility and integration: retrieval-augmented generation keeps knowledge outside the model but only provides prompt-level augmentation, whereas post-training based methods encode new knowledge into shared parameters but may introduce catastrophic forgetting, knowledge conflict, and costly updates. In this paper, we propose Decoupled Mixture-of-Experts (DMoE), a modular architecture for parametric knowledge injection that decouples both experts and the router from the base model. DMoE converts external knowledge c...


## Candidate 039

Query: continual learning for neural networks

Likely paper IDs:

1. `2606.14459v1` score=0.3369
   Title: MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition
   Categories: cs.CL, cs.AI, cs.SD
   Abstract: Modern Automatic Speech Recognition (ASR) systems have made remarkable progress on standard benchmarks, yet performance gaps have emerged under real-world distribution shifts, caused by recording conditions, accents, speech impairments, and noise. Existing datasets and benchmarks typically isolate these factors, which overlooks their co-occurrence in real-world applications. In this paper, we argue that model robustness can be treated as a dynamic capability that continually develops, and we introduce MoDiCoL, a Modular Diagnostic Continual Learning dataset designed for controlled analysis of linguistic content, speaker characteristics, and acoustic environments. Furthermore, we propose a re...

2. `2606.07474v1` score=0.3285
   Title: Unsupervised Continual Clustering via Forward-Backward Knowledge Distillation
   Categories: cs.LG
   Abstract: Unsupervised Continual Learning (UCL) aims to enable neural networks to learn sequential tasks without labels or access to past data. A major challenge in this setting is Catastrophic Forgetting, where models forget previously learned tasks upon learning new ones. This challenge is amplified in UCL due to the absence of labels to guide learning and memory retention. Existing mitigation strategies, such as knowledge distillation and replay buffers, often raise memory and privacy concerns. Moreover, current UCL methods largely overlook clustering-specific objectives. To fill this gap, we introduce Unsupervised Continual Clustering (UCC) and propose Forward-Backward Knowledge Distillation for C...

3. `2606.07247v2` score=0.2836
   Title: Theory of learning of high-dimensional controlled non-linear dynamical systems (I): models and methods
   Categories: cond-mat.dis-nn, cond-mat.stat-mech, stat.ML
   Abstract: Neural ordinary differential equations (neural ODEs) have rapidly gained prominence as a powerful and unifying framework for conceptualizing artificial neural networks, elegantly connecting the continuous-time modeling of dynamical systems with the discrete, data-driven paradigm of modern deep learning. Beyond their practical advantages they offer fresh theoretical insights into the training and generalization properties of neural networks. The distinctive feature of this framework is its dual dynamical nature: inference dynamics, which govern the ODE evolution during forward computation, and training dynamics, which control the optimization of model parameters. This makes neural ODEs a part...

4. `2606.14883v1` score=0.2812
   Title: Understanding Cross-Modal Contributions in Continual Vision-Language Models: A Theoretical Perspective
   Categories: cs.CV, cs.LG
   Abstract: Continual vision-language models are commonly addressed through sequential fine-tuning; however, although this paradigm enables adaptation to new environments (tasks), it inherently emphasizes the contribution of previously learned environments (tasks) at the expense of the stability required to preserve previously acquired knowledge. While existing approaches have adequately studied continual learning and catastrophic forgetting in vision-language models (VLMs), the theoretical understanding of modality-specific contributions across a sequence of environments remains largely unexplored. In this paper, we present a new theoretical perspective to understand the cross-modal (vision-language) c...

5. `2606.07500v1` score=0.2650
   Title: Sparse Subspace-to-Expert Sharing for Task-Agnostic Continual Learning
   Categories: cs.LG, cs.AI
   Abstract: Continual learning in Large Language Models (LLMs) is hindered by the plasticity-stability dilemma, where acquiring new capabilities often leads to catastrophic forgetting of previous knowledge. Existing methods typically treat parameters uniformly, failing to distinguish between specific task knowledge and shared capabilities. We introduce Mixture of Sparse Experts for Task Agnostic Continual Learning (SETA), a framework that resolves the plasticity-stability conflict through adaptive sparse subspace decomposition into task-specific expert modules. Unlike standard updates, where tasks compete for the same parameters, SETA separates knowledge into unique experts, designed to isolate task-spe...

6. `2606.09762v1` score=0.2609
   Title: Preserving Plasticity in Continual Learning via Dynamical Isometry
   Categories: cs.LG, cs.AI
   Abstract: Continual training of deep neural networks under non-stationarity often leads to a progressive loss of plasticity, eventually limiting further learning. We relate plasticity to the empirical Neural Tangent Kernel, and identify dynamical isometry (the condition that layer-wise Jacobian singular values remain close to one) as a key mechanism for preserving plasticity in continual learning. We revisit a class of networks that are almost-everywhere isometric while remaining universal Lipschitz function approximators, demonstrating that near-dynamical isometry is compatible with expressive nonlinear representations. For general architectures, we propose an efficient isometry-promoting regularizat...

7. `2606.11844v1` score=0.2593
   Title: TaskFusion: Continual Anomaly Detection for Heterogeneous Tabular Data
   Categories: cs.LG
   Abstract: Continual anomaly detection in tabular data is challenging and remains largely underexplored, particularly in settings with heterogeneous feature schemas, distribution shifts, and severe class imbalance. In many real-world applications, data arrive sequentially from diverse domains, rendering conventional continual learning methods ineffective due to their reliance on a fixed input space. We propose a continual learning (CL) method, which can overcome these challenges and continually learn from different tasks. Our method consists of three main parts: our AGF model, Taskfusion augmentation, and outlier exposure. The AGF-model maps task-specific features into a shared space, then aligns distr...

8. `2606.08452v1` score=0.2558
   Title: Theoretical Foundations of Continual Learning via Drift-Plus-Penalty
   Categories: cs.LG
   Abstract: In many real-world settings, data streams are nonstationary and arrive sequentially, requiring learning systems to adapt continuously without retraining from scratch. Continual learning (CL) addresses this challenge by incorporating new tasks while mitigating catastrophic forgetting, where learning new information degrades performance on previously acquired knowledge. We introduce a control-theoretic perspective on CL that explicitly regulates the evolution of forgetting, framing adaptation as a controlled process subject to long-term stability constraints. We focus on replay-based CL, where a finite memory buffer stores representative samples from prior tasks. We propose COntinual Learning ...


## Candidate 040

Query: domain adaptation for computer vision

Likely paper IDs:

1. `2606.07489v2` score=0.2872
   Title: How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope
   Categories: cs.AI, econ.GN
   Abstract: Frontier AI systems are bridging the gap between intelligence and utility by shifting from conversational assistants to autonomous agents that execute tasks end to end. Using production data from Perplexity's Search and Computer products, we study this transition by examining how AI agents accelerate and reshape knowledge work. Three key empirical findings emerge. First, using sessions with near-identical initial query pairs as natural experiments for the same underlying task attempted with both products, Computer performs 26 minutes of autonomous work per user session, versus 33 seconds for Search. Computer automates task decomposition and execution that Search users might otherwise manuall...

2. `2606.14023v1` score=0.2375
   Title: Geometric Domain Adaptation via Optimal Transport for Linear Regression in R^2
   Categories: stat.ML, cs.LG, stat.ME
   Abstract: Optimal Transport has become recently a powerful method for domain adaptation by aligning source and target distributions. We study a supervised domain adaptation problem where source and target domains are related by a rotation or a translation or a homothety in $\mathbb{R}^2$. We prove that the optimal transport map recovers the underlying map when using a $p-$norm cost with $p \geq 2$. Based on this insight, we develop a method combining $K-$means and optimal transport to estimate the underlying map, enabling adaptation of linear regression models when target data is scarce. Simulations demonstrate improved performance over baseline methods. Rather than relying on highly expressive deep l...

3. `2606.18472v1` score=0.2176
   Title: Domain Generalizable Adaptation of 3D Vision-Language Models via Regularized Fine-Tuning
   Categories: cs.CV
   Abstract: Domain adaptation remains a central challenge in 3D vision, especially for multimodal foundation models that align 3D point clouds with visual and textual data. While these models demonstrate strong general capabilities, adapting them to downstream domains with limited data often leads to overfitting and catastrophic forgetting. To address this, we introduce ReFine3D, a regularized fine-tuning framework designed for domain-generalizable tuning of 3D large multimodal models (LMMs). ReFine3D combines selective layer tuning with two targeted regularization strategies: multi-view consistency across augmented point clouds and text diversity through synonym-based prompts generated by large languag...

4. `2606.19266v1` score=0.2086
   Title: Trade-offs in Medical LLM Adaptation: An Empirical Study in French QA
   Categories: cs.CL, cs.AI
   Abstract: The development of large language models (LLMs) has led to an increased focus on their adaptation to specialized domains and languages, yet the effectiveness of domain adaptation strategies remains unclear. We present a study of medical domain adaptation using French medical question-answering (QA) as a case study. We compare continual pretraining (CPT), supervised fine-tuning (SFT), and their combination across three model families, multiple sizes, and three initialization types, explicitly disentangling adaptation effects from base model choice. We evaluate both multiple-choice (MCQA) and open-ended QA (OEQA) under greedy and constrained decoding using automatic metrics and LLM-as-a-Judge ...

5. `2606.14578v1` score=0.1953
   Title: A Qualitative Review of GenAI-Based Methods for Data Generation and Augmentation in Industrial Computer Vision Applications
   Categories: cs.CV
   Abstract: AI-driven computer vision applications require a profound database to ensure predictable behaviors and performance. Such predictable behaviors are especially important for industrial applications in gaining trust from users. However, such a database is not readily available in industrial applications, and its acquisition is not trivial either. Active learning methods can be applied to ramp up data within a project deployment to iteratively increase the database, and thus the application predictability. Unfortunately, we observe that this often leads to a loss of user trust in the application, which is difficult to regain once lost. This leads to a "chicken-and-egg" dilemma in which neither t...

6. `2606.15117v1` score=0.1856
   Title: Teacher-Student Structure for Domain Adaptation in Ensemble Audio-Visual Video Deepfake Detection
   Categories: cs.MM, cs.AI, cs.CV, cs.LG, cs.SD
   Abstract: The rapid advancement of generative AI models is leading to more realistic deepfake media, encompassing the manipulation of audio, video, or both. This raises severe privacy and societal concerns. Numerous studies in this area have yielded promising intra-domain results; however, these models frequently exhibit decreased efficacy when faced with data from dissimilar domains. Consequently, recent deepfake detection approaches focus on enhancing the generalization ability through multiple techniques that incorporate all input modalities, including audio, images, and their interactions. In this regard, we propose the EAV-DFD method, a generalized deep ensemble audio-visual model (EAV-DFD) combi...

7. `2606.14222v1` score=0.1790
   Title: Learning the Context of Errors: Black-Box Online Adaptation of Time Series Foundation Models
   Categories: cs.LG
   Abstract: The rapid evolution of Time Series Foundation Models (TSFMs) has advanced zero-shot forecasting across diverse domains. Inspired by the current form of Large Language Models, future TSFMs may be offered as commercialized, closed-source API services. However, many existing online adaptation methods still rely on white-box access for parameter fine-tuning or gradient backpropagation. This paradigm mismatch raises a question: In black-box online adaptation for TSFMs, what should we learn? We answer this with an insight: the predictive errors of the base model are conditioned on both the input and output of the base model (i.e., the context of errors). To validate this insight, we propose ORCA (...

8. `2606.20272v1` score=0.1784
   Title: Efficiently Linking Real Scenes with Synthetic Data Generation for AI-based Cognitive Robotics and Computer Vision Applications
   Categories: cs.RO, cs.CV
   Abstract: AI vision models are a driving factor for the potential use case scenarios of cognitive robotics within in the industry and household applications. A large array of methods from semantic environment analysis towards 6D and grasping pose estimation have been proposed based on the latest AI achievements. However, such advancements require further strong and efficient methods w.r.t. training data and AI-architectures, which are capable in synergy to tackle current challenges, precision limits, and scalability beyond domain gaps. In this paper, we discuss these current limits and trends in the related state-of-the-art which are challenging those. Further we discuss our current work in progress o...


## Candidate 041

Query: remote sensing image understanding with foundation models

Likely paper IDs:

1. `2606.17020v1` score=0.2974
   Title: FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models
   Categories: cs.CV, cs.AI
   Abstract: Remote sensing vision-language models have advanced Earth observation understanding, but most existing work remains centered on RGB imagery, leaving the complementary information in infrared data underexplored. Infrared images provide distinctive cues, including thermal intensity structures, object boundaries, and illumination-invariant scene features, which can enrich visual-language learning beyond conventional RGB observations. However, a large-scale RGB-infrared-text dataset for remote sensing vision-language modeling is still absent. To address this gap, we introduce FusionRS, the first large-scale RGB-infrared-text dataset designed for dual-modal vision-language learning in remote sens...

2. `2606.16124v1` score=0.2161
   Title: Training-Free Open-Vocabulary Visual Grounding for Remote Sensing Images and Videos
   Categories: cs.CV
   Abstract: Remote sensing visual grounding (RSVG) aims to localize a referred target in a remote sensing image or video according to a natural language expression. Existing RSVG methods usually rely on task-specific manual annotations, which are costly to collect and inevitably limited in covering the diversity of real-world geospatial scenarios. As a result, they often struggle to generalize to open-vocabulary queries involving novel objects, fine-grained attributes, complex spatial relationships, and functional semantics. In this paper, we propose RSVG-ZeroOV, a training-free framework that leverages frozen generic foundation models for zero-shot open-vocabulary RSVG. RSVG-ZeroOV follows an Overview-...

3. `2606.19277v1` score=0.2102
   Title: A Unified Framework for Efficient Remote Sensing Visual Question Answering: Adapting Dual, Hybrid, and Encoder-Decoder Architectures
   Categories: cs.CV
   Abstract: Visual Question Answering (VQA) in the Remote Sensing (RS) domain presents unique challenges due to the high resolution, multi scale object distribution, and semantic complexity of aerial imagery. While general domain Foundation Models have achieved remarkable success, their direct application to RSVQA is hindered by massive domain shifts and the computationally prohibitive nature of full fine tuning. This study presents a comparative analysis of RS Adapter, a Parameter Efficient Fine Tuning (PEFT) strategy, applied across three distinct Vision Language Model (VLM) architectures: the Dual Encoder CLIP, the Encoder Decoder BLIP, and the Hybrid FLAVA. We introduce a unified architectural surge...

4. `2606.08535v1` score=0.2018
   Title: NGram-MoSE: Efficient Remote Sensing Super-Resolution via N-Gram Context and Mixture-of-Experts
   Categories: cs.CV
   Abstract: Remote sensing applications for environmental monitoring and disaster management are frequently constrained by a spatial--temporal trade-off: imagery with fine spatial detail is often acquired less frequently, whereas more temporally available observations are typically coarser. Single-image super-resolution provides a practical means to enhance coarse imagery without changing acquisition schedules, yet many Transformer-based SR models remain computationally expensive and can be sensitive to limited or geographically biased training data, which degrades robustness under out-of-distribution conditions. This paper presents NGram-MoSE, a lightweight Transformer architecture designed to improve ...

5. `2606.20177v1` score=0.1868
   Title: Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs
   Categories: cs.CV, cs.AI
   Abstract: Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in various Remote Sensing (RS) tasks. However, their ability to comprehend negation remains underexplored, limiting deployment in real-world applications where models must explicitly identify what is false or absent, e.g., emergency responders need to locate non-flooded routes for evacuation. To comprehensively study this limitation, we introduce RS-Neg, the first benchmark to evaluate negation understanding across region-level to scene-level tasks. Specifically, we design an automated data generation pipeline for RS imagery, using LLMs to synthesize diverse negation queries, and introduce a dynamic visual focus mo...

6. `2606.13896v1` score=0.1817
   Title: How do Self-Supervised Remote Sensing Vision Models Transfer to Downstream Tasks?
   Categories: cs.CV, cs.AI
   Abstract: Self-supervised geospatial foundation models (GeoFMs) learn transferable representations from remote sensing data, but their downstream behavior is difficult to characterize. We study six representative GeoFMs spanning joint-embedding, reconstruction, and multimodal pretraining families, and evaluate transfer across classification, regression, and segmentation benchmarks under different label availability and downstream pipelines. We find that model rankings change across tasks and adaptation settings. Layerwise probing shows that, in most cases, task-relevant information is more accessible in intermediate transformer blocks compared to final-layer embeddings, and that GeoFMs exhibit distinc...

7. `2606.10701v1` score=0.1784
   Title: Vector Map as Language: Toward Unified Remote Sensing Vector Mapping
   Categories: cs.CV
   Abstract: Remote sensing vector mapping aims to generate structured maps of geospatial entities, such as buildings, roads, and water bodies, from remote sensing imagery. In practice, vector maps usually contain multiple category layers and heterogeneous entity structures, requiring a unified model for diverse mapping needs. However, existing methods typically represent vector objects as polygons or graphs, making them suitable only for specific categories: polygons poorly capture topological relations, while graphs often blur instance boundaries. We observe that language, as a natural medium for human communication, offers a flexible and expressive representation that can accommodate heterogeneous map...

8. `2606.16255v1` score=0.1722
   Title: UniDDT: Unifying Multimodal Understanding and Generation with Decoupled Diffusion Transformer
   Categories: cs.CV
   Abstract: Unified Multimodal Models (UMMs) have emerged as a critical direction for general-purpose multimodal intelligence, integrating understanding and generation into a single framework. However, existing UMMs face prominent challenges: (1) the inherent learning conflicts between visual understanding and generation tasks, leading to suboptimal modeling in both tasks; (2) different understanding and generation visual spaces impeding scalability; (3) over-reliance on task-specific data that neglects the duality of text-image understanding and generation. To address these challenges, we propose UniDDT, which leverages a Noisy ViT encoder along with an LLM to unify semantic encoding for visual generat...


## Candidate 042

Query: autonomous driving perception with multimodal learning

Likely paper IDs:

1. `2606.17362v1` score=0.3737
   Title: DriveJudge: Rethinking Autonomous Driving Evaluation with Vision-Language Models
   Categories: cs.CV, cs.AI, cs.LG, cs.RO
   Abstract: Autonomous driving has shifted towards end-to-end policy learning, where reliable, interpretable policy evaluation is a fundamental challenge as driving quality is highly context-dependent. Commonly used rule-based driving metrics like EPDMS are interpretable but lack context-awareness, while recent VLMbased evaluations are context-aware but limited by ambiguous VLM outputs and weak physical grounding. To evaluate driving in a manner that is both interpretable and context-aware, we introduce DriveJudge. DriveJudge is a driving evaluation agent that combines rule-grounded evaluation with Vision-Language Model (VLM) reasoning and selectively invokes physically-grounded deterministic rule funct...

2. `2606.13840v1` score=0.3015
   Title: Multi-Agent Embodied Autonomous Driving: From V2X Information Exchange to Shared World Models
   Categories: cs.RO, cs.CV
   Abstract: Autonomous driving is shifting from isolated vehicle intelligence toward multi-agent embodied systems that share perception, infer intent, and coordinate action under uncertainty. This survey examines this transition through the lens of Shared World Models (SWMs): predictive cross-agent representations maintained across vehicles, infrastructure, and other traffic participants. We review more than 380 publications spanning vehicle-to-everything (V2X) communication, collaborative perception, inter-agent cognition, cooperative planning, end-to-end cooperative driving, and simulation and data engines for closed-loop validation. The organizing question is how exchanged observations become aligned...

3. `2606.19836v1` score=0.3004
   Title: World Engine: Towards the Era of Post-Training for Autonomous Driving
   Categories: cs.RO, cs.CV
   Abstract: Autonomous vehicles must operate safely in the real world, where errors can have severe consequences. Although modern end-to-end driving policies excel in routine scenarios, their reliability is limited by the scarcity of safety-critical ``long-tail'' events in real driving datasets. These rare interactions define the practical safety boundary of the learned policy, yet they are difficult to collect at scale in the real world. Here we show that this fundamental limitation can be addressed by post-training pre-trained driving models on synthesized high-stakes interactions. We introduce World Engine, a generative framework that reconstructs high-fidelity interactive environments from real-worl...

4. `2606.09569v1` score=0.2948
   Title: Efficient Minimal Solvers for Relative Pose Estimation in Autonomous Driving Applications
   Categories: cs.RO, cs.CV
   Abstract: With the advancement of visual sensing systems, computer vision is playing an increasingly important role in autonomous driving and robot navigation. Relative pose estimation in multi-camera systems is essential for accurate vehicle localization and environment perception, demanding high real-time performance and robustness. Existing methods, however, often involve high computational costs and rely heavily on abundant feature matches, limiting their applicability in time-sensitive driving scenarios. To address these limitations, this paper introduces a unified framework for efficient relative pose estimation, built upon a novel translation parameterization and first-order rotation approximat...

5. `2606.14766v1` score=0.2811
   Title: XMedFusion: A Knowledge-Guided Multimodal Perception and Reasoning Framework for Autonomous Medical Systems
   Categories: cs.CV, cs.AI, cs.MA
   Abstract: Autonomous medical and robotic systems increasingly rely on intelligent perception and reasoning capabilities to interpret visual data and support clinical decision making. Radiology report generation represents a critical component of such automated diagnostic workflows, yet existing end-to-end multimodal models often suffer from weak visual grounding, resulting in unreliable interpretations and omission of subtle clinical findings. This paper presents XMedFusion, a modular AI framework designed as an intelligent perception and reasoning module for autonomous medical systems. The proposed framework decomposes visual information into coordinated functional components that emulate expert-driv...

6. `2606.08525v2` score=0.2690
   Title: DriveReward: A Comprehensive Dataset and Generative Vision-Language Reward Model for Autonomous Driving
   Categories: cs.CV
   Abstract: Reward models play a pivotal role in reinforcement learning (RL) and multi-modal trajectory selection for autonomous driving. However, acquiring such rewards typically relies on hand-crafted rule-based objectives or perception ground truth, which hinders generalization for data-scaling. While Vision-Language Models (VLMs) have demonstrated feasibility as reward models in other domains, their effectiveness in driving tasks remains underexplored. In this work, we bridge this gap by (1) introducing DriveReward, a reasoning trajectory evaluation dataset rigorously labeled via temporally-grounded visual guidance, and augmented with counterfactual driving behaviors., (2) alongside a specialized Vi...

7. `2606.19534v1` score=0.2559
   Title: PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models
   Categories: cs.CV, cs.AI, cs.CL
   Abstract: Multimodal large language models (MLLMs) have achieved remarkable progress in visual understanding tasks. However, most existing MLLMs rely on autoregressive generation, which limits their efficiency for perception tasks that require captioning multiple regions. In this work, we propose PerceptionDLM, a multimodal diffusion language model optimized for efficient parallel region perception. Built upon PerceptionDLM-Base, a strong foundational baseline that achieves state-of-the-art performance among open-source diffusion MLLMs, our architecture fully leverages the parallel decoding nature of DLMs. Specifically, we introduce efficient prompting and structured attention masking to enable simult...

8. `2606.09362v1` score=0.2556
   Title: Zero-Shot Semantic Re-Identification for Autonomous Driving: A VLM Baseline Study
   Categories: cs.CV, cs.LG
   Abstract: Re-Identification (ReID) in autonomous driving is typically formulated as a visual matching problem, where observations of vehicles, pedestrians, and cyclists are associated across time, frames, or camera views using learned appearance embeddings, often complemented by motion, geometric, or multimodal cues. However, purely visual representations may be sensitive to viewpoint, occlusion, illumination, and sensor-domain variations, limiting their interpretability and robustness in complex driving scenes. We propose a baseline study of a zero-shot pipeline using Vision-Language Models (VLMs) to generate textual descriptions of detected traffic participants and evaluate whether these description...


## Candidate 043

Query: anomaly detection using deep learning

Likely paper IDs:

1. `2606.09670v1` score=0.4279
   Title: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
   Categories: cs.CV, cs.AI
   Abstract: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentat...

2. `2606.11844v1` score=0.4147
   Title: TaskFusion: Continual Anomaly Detection for Heterogeneous Tabular Data
   Categories: cs.LG
   Abstract: Continual anomaly detection in tabular data is challenging and remains largely underexplored, particularly in settings with heterogeneous feature schemas, distribution shifts, and severe class imbalance. In many real-world applications, data arrive sequentially from diverse domains, rendering conventional continual learning methods ineffective due to their reliance on a fixed input space. We propose a continual learning (CL) method, which can overcome these challenges and continually learn from different tasks. Our method consists of three main parts: our AGF model, Taskfusion augmentation, and outlier exposure. The AGF-model maps task-specific features into a shared space, then aligns distr...

3. `2606.10827v1` score=0.3972
   Title: A Unified Siamese Learning Framework for Zero-Day Anomaly Detection and Classification in Optical Networks
   Categories: cs.NI, cs.AI
   Abstract: A multi-similarity Siamese neural network unifies zero-day anomaly detection and one-shot classification in optical networks, achieving over 99% accuracy and instant adaptability across lightpaths and unseen anomaly types without any retraining.

4. `2606.19255v1` score=0.3418
   Title: SCAN: Enhance Time Series Anomaly Detection via Multi-Scale Neighborhood-Centered Clustering
   Categories: cs.LG
   Abstract: Time series anomaly detection plays a crucial role in a wide range of real-world applications. Reconstruction-based methods have become the mainstream paradigm, but they suffer from over-generalization and under-generalization problems, which are challenging to balance. To address this, we introduce multi-scale clustering to enhance reconstruction-based methods. At the representation level, we integrate the cluster center representations of normal patterns to constrain the model to target representative normal patterns for reconstruction, preventing dominance of powerful capacity and representation capability. At the anomaly criterion level, we derive anomaly confidence score based on cluste...

5. `2606.15280v1` score=0.3401
   Title: Rethinking Structural Anomaly Detection: From Decision Boundaries to Projection Operators
   Categories: cs.LG
   Abstract: Most existing anomaly detection methods rely on estimating a probability density or learning an enclosing decision boundary, implicitly assuming that normal data occupies a region of non-zero volume in the ambient space. In contrast, structural anomaly detection considers data that lies near a low-dimensional manifold, creating a mismatch between the inductive bias of existing methods and the structure of the data, often resulting in degraded performance. To address this mismatch, we introduce a geometric perspective. Specifically, we learn a projection operator onto the manifold of normal samples and define a sample as anomalous if it is altered by this projection. This formulation naturall...

6. `2606.12483v1` score=0.3256
   Title: Scalable anomaly detection via a univariate Christoffel function
   Categories: cs.LG
   Abstract: Anomaly detection plays a critical role in identifying unusual patterns across domains such as fraud detection, network intrusion, and system fault diagnosis. Recently, Christoffel function-based methods, rooted in polynomial optimization, have emerged as promising alternatives to deep learning due to their strong mathematical foundations and computational frugality. However, their practical applicability is hindered by the need to invert a matrix whose size grows exponentially with the data dimension, rendering the method intractable even for moderate-dimensional datasets. This paper addresses the dimensionality limitations of Christoffel function-based anomaly detection while preserving it...

7. `2606.18749v1` score=0.3164
   Title: Toward Training-Free Zero-Shot Anomaly Detection in 3D Medical Images: A Batch-Based Approach Using 2D Foundation Models
   Categories: cs.CV
   Abstract: Zero-shot anomaly detection (ZSAD) is attractive for medical imaging because clinical systems must handle heterogeneous acquisition protocols, changing patient populations, and pathologies for which annotated training data may be unavailable. Most existing zero-shot anomaly detection methods are designed for 2D images, and their direct extension to 3D medical volumes is limited by the scarcity of large-scale volumetric foundation models or by the difficulty of utilizing volumetric context. We propose CS3F, a training-free batch-based framework for ZSAD in 3D medical images using 2D foundation models. Each volume is decomposed along multiple anatomical axes and encoded slice-wise by a 2D visi...

8. `2606.14129v1` score=0.2977
   Title: BoRAD: Bootstrap your Own Representations for Multi-class Anomaly Detection
   Categories: cs.CV
   Abstract: Reconstruction-based anomaly detection is attractive for industrial inspection, but scaling it from category-specific training to a one-for-all setting is challenging. A single model must reconstruct diverse normal appearances without copying abnormal details, which exposes two coupled failure modes: identical shortcut, where anomalies pass through the reconstruction path, and mis-reconstruction, where normal categories are confused with one another. We propose \textbf{BoRAD}, a label-free training framework that treats this as a representation-capacity allocation problem. BoRAD uses a shared learnable prototype bank to impose two complementary regularizers: spatial prototype alignment contr...


## Candidate 044

Query: AI generated image detection

Likely paper IDs:

1. `2606.07219v1` score=0.3536
   Title: Adversarial Creation and Detection of AI-Generated Social Bot Content
   Categories: cs.CL, cs.SI
   Abstract: The convergence of large language models and social bots allows malicious actors to manipulate the information ecosystem by generating human-like content at scale. Existing models for detecting AI-generated content often fail in the wild, primarily due to the lack of ground-truth data. We address this gap through an adversarial methodology that models the impersonation of real social media users by malicious actors. Using this methodology, we curate a multilingual, cross-platform dataset of paired human and AI-generated messages. Training on such adversarial data yields accurate detection of AI-generated text. Our approach significantly outperforms existing models for content-based bot detec...

2. `2606.19259v1` score=0.3158
   Title: A Multi-Domain Benchmark for Detecting AI-Generated Text-Rich Images from GPT-Image-2
   Categories: cs.CV, cs.AI
   Abstract: Text-rich images often contain privacy-sensitive, transactional, or decision-relevant information. As recent multimodal image generation models become increasingly capable of synthesizing realistic textual content and structured visual designs, detecting AI-generated text-rich images has become an important challenge for digital trust and content authenticity. Existing benchmarks, however, largely focus on object-centric images and provide limited coverage of scenarios where textual semantics and layout organization are central. In this paper, we introduce a multi-domain benchmark for detecting text-rich images generated by OpenAI's GPT Image 2. The benchmark contains 8,602 images across six...

3. `2606.16742v1` score=0.3145
   Title: Revealing Artifacts via Noise Amplification: A Novel Perspective for AI-Generated Video Detection
   Categories: cs.CV, cs.AI
   Abstract: With the rapid advancement of video generation models, distinguishing between AI-generated and authentic videos has emerged as a challenging endeavor. The majority of existing research endeavors concentrate on the development of detectors for identifying samples generated by generative adversarial networks. Nevertheless, the detection of AI-generated videos, particularly those produced by text-to-video models, still remains an uncharted territory. Although state-of-the-art text-to-video models can generate realistic visual content similar to real videos, they fall short of generating the details of the images and the changes in details within the videos. Inspired by this, we address AI-gener...

4. `2606.12620v1` score=0.2742
   Title: HybridCodeAuthorship: A Benchmark Dataset for Line-Level Code Authorship Detection
   Categories: cs.SE, cs.AI
   Abstract: Thanks to the rapid adoption of AI code assistants powered by large language models (LLMs), industry codebases are, increasingly, a hybrid of AI- and human-authored code. For risk management and productivity analysis purposes, it is crucial to enable fine-grained location detection of AI-generated code. To develop algorithms for this task, quality benchmarks are needed to assess performance. However, existing benchmarks tend to comprise academic, LeetCode-style problems and presume a code snippet is either completely human-authored or completely AI-authored, which is not reflective of the diverse intents and styles of industry codebases utilizing AI code assistants. To fill these gaps, we in...

5. `2606.14787v1` score=0.2705
   Title: Vision-Encoder Behavioral Fingerprints of Image-to-Image Generative Models: A Training-Paradigm-Driven Taxonomy of Six Commercial APIs
   Categories: cs.CV, cs.CR
   Abstract: We study six production image-to-image AI systems (gpt-image-1, Gemini 2.5 Flash Image, Flux Kontext, SDXL img2img, SD3 img2img, and Qwen Image Edit) under a content-adaptive sub-JND adversarial perturbation pipeline, scoring all outputs by frozen DINOv2 ViT-B/14 token distances against clean references. Across a 3,588-call corpus spanning COCO photographs, CelebA-HQ portraits, and AI-generated inputs, the six systems partition into two image-invariant behavioral bands on a 2D (patch_mean, ssim_clean) plane: edit-trained models (Flux Kontext, Qwen Edit, Gemini) cluster in a tight band, while T2I-base models adapted at sampling time (SDXL, SD3, gpt-image-1) cluster in a drift band.

6. `2606.08634v1` score=0.2648
   Title: SSAFE: Simple and Strong AI-Generated Image Detection via Frozen Vision Encoders
   Categories: cs.CV
   Abstract: The rapid advancement of generative models has blurred the boundary between synthetic and real imagery, creating an urgent need for reliable deepfake detection. Yet most existing approaches rely on massive real--fake datasets, which are increasingly difficult to maintain as new generators continue to emerge. In this work, we investigate how much information about image authenticity is already encoded in modern multimodal vision representations. We find that frozen multimodal encoders naturally separate real and synthetic images in their embedding space, enabling a simple linear classifier to achieve strong performance without task-specific fine-tuning. Motivated by this observation, we devel...

7. `2606.12350v1` score=0.2491
   Title: Nonslop: A Gamified Experiment in Human-AI Collaborative Writing
   Categories: cs.AI
   Abstract: The rapid proliferation of large language models (LLMs) raises critical questions about human creativity and individual expression in an era of AI-assisted creation. When do humans adopt AI suggestions, and what are the implications for individual voice? This study examines these questions through a gamified writing exercise where 74 participants (214 responses) replied to prompts while AI-generated word suggestions were available as they wrote. The game simulates a dystopian future in which an AI is attempting to learn from what remains of human individuality, and disincentivizes AI-like writing. In doing so, it attempts to create conditions that reveal authentic user preferences rather tha...

8. `2606.11533v1` score=0.2348
   Title: AI Researchers Must Help Lead Arms Control to Mitigate Military AI Risks
   Categories: cs.CY, cs.AI, cs.ET, cs.LG
   Abstract: The advancement of AI capabilities compels researchers and the public to be more aware of its potential worldwide impact. A pressing near-term concern is the regulation of military AI applications. Armament manufacturers and defense contractors are increasingly investing in AI capabilities and forging partnerships with AI companies, creating a burgeoning coalition that demands military leaders, arms control diplomacy experts, and AI researchers collaborate to ensure a safer future. While AI researchers often focus on the long-term implications of superintelligent AI, this approach may not adequately address the immediate challenges posed by AI in military applications. Success requires ackno...


## Candidate 045

Query: audio language models and speech understanding

Likely paper IDs:

1. `2606.13507v1` score=0.5076
   Title: Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data
   Categories: cs.CL
   Abstract: Large-scale mined corpora provide abundant training data for end-to-end speech-to-speech translation (S2ST) but may contain noise, misalignment, and semantic errors. Filtering noisy data is crucial to maintain robust speech translation performance. We study how to train an audio-language model to make keep/drop decisions on paired speech directly from audio. To obtain reliable supervision without manual labels, we adopt a scalable two-stage Rank-to-Distill strategy. A lightweight ranker generates keep/drop pseudo-labels from noisy speech pairs, then trains an audio large language model to predict keep/drop directly from raw paired speech. The resulting model jointly captures acoustic fidelit...

2. `2606.18273v1` score=0.5006
   Title: Continuous Audio Thinking for Large Audio Language Models
   Categories: cs.CL, cs.AI, cs.SD, eess.AS
   Abstract: Large audio language models (LALMs) have shown impressive capabilities on diverse audio understanding tasks, ranging from speech transcription to music analysis. However, because LALMs are typically trained to produce text-aligned responses, their hidden states are progressively shaped for text generation rather than for preserving acoustic information. As a result, the diverse acoustic content that audio carries, such as phonetic detail, prosody, sound events, affect, and pitch, is lost along the way and difficult to leverage in the response. We introduce Continuous Audio Thinking (CoAT), a framework that equips audio language models with a continuous latent workspace for organizing acousti...

3. `2606.11033v1` score=0.4840
   Title: AuRA: Internalizing Audio Understanding into LLMs as LoRA
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: Recent efforts to extend large language models (LLMs) to speech inputs typically rely on cascaded ASR-LLM pipelines, end-to-end speech-language models, or bridge/distillation-based adaptation. While these routes respectively reuse strong pretrained components, enable native speech-language interaction, or offer lightweight adaptation, they often suffer from transcript-interface latency, costly multimodal training, or sequential speech-language coupling. To address these limitations, we present AuRA, a method that distills audio encoding capability into the LLM. Specifically, AuRA feeds the same speech input to an ASR encoder (as a teacher) and a LoRA-adapted LLM (as a student) through a ligh...

4. `2606.10246v1` score=0.4327
   Title: Linguistically Augmented Audio Speech Data (LinguAS)
   Categories: cs.SD, cs.AI, cs.LG
   Abstract: Maliciously-created fake speech, including deepfaked and spoofed audio, is proliferating at an alarming rate, and detection models are racing to stay ahead of the curve. Yet, most detection models are trained to make inference on frame-level audio features alone without leveraging valuable linguistic cues at larger timescales. To address this gap, we present Linguistically Augmented Audio Speech Data (LinguAS), a dataset of genuine and deepfaked audio samples annotated with five strategically-chosen, Expert-Defined Linguistic Features (EDLFs) that occur frequently in spoken English and are characteristic of natural human speech. LinguAS contains over 800 audio samples, each of which are anno...

5. `2606.10738v1` score=0.4103
   Title: Spatial-Omni: Spatial Audio Understanding Integration in Multimodal LLMs via FOA Encoding
   Categories: eess.AS, cs.AI
   Abstract: Recent multimodal large language models mainly process audio as monaural signals, thereby discarding the spatial cues contained in spatial audio for sound localization, spatial relation reasoning, and spatial scene understanding. We propose Spatial-Omni, a lightweight method that implements SO-Encoder to inject First-Order Ambisonics (FOA) spatial audio into existing Omni LLMs as an independent modality, without modifying their original audio encoders. SO-Encoder provides spatial tokens with limited additional context cost and improves spatial audio understanding through efficient staged training. To support training and evaluation, we construct SO-Dataset, SO-QA, and SO-Bench from open-sour...

6. `2606.14591v1` score=0.4021
   Title: AudioDER: A Deduplication-Enhanced Reasoning Dataset for Post-Training Large Audio-Language Models
   Categories: cs.SD, cs.AI
   Abstract: Large Audio-Language Models (LALMs) have shown strong performance on a wide range of audio understanding tasks, yet they still struggle with complex audio reasoning. A practical way to improve such capabilities is post-training, whose effectiveness critically depends on the quality and diversity of training data. However, existing audio-language datasets often contain substantial redundancy, where many samples are highly similar in acoustic content and thus provide overlapping supervisory signals. Such redundancy not only increases annotation cost, but also limits corpus diversity and reduces the effectiveness of post-training. To address this issue, we propose a redundancy-aware data constr...

7. `2606.17417v1` score=0.3999
   Title: A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models
   Categories: cs.SD, cs.LG
   Abstract: Large Audio Language Models (LALMs) achieve strong performance on a variety of audio understanding tasks but continue to struggle with temporal reasoning, a fundamental capability central to human auditory perception. Understanding the causes of these failures remains challenging as existing benchmarks report performance gaps without probing underlying mechanisms. To address this, we introduce a benchmark with 1,657 questions across three foundational tasks designed specifically for mechanistic analysis. Examining model outputs across varying input settings (behavioral analysis) reveals that models often under-utilize audio when textual cues are available. We also provide the first causal me...

8. `2606.15751v1` score=0.3758
   Title: Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models
   Categories: cs.SD, cs.LG, cs.MM, eess.AS
   Abstract: Audio-Language Models (ALMs) have shown remarkable success in zero-shot audio classification by aligning audio waveforms with text. Recent efforts to improve downstream performance focus on learning optimal text prompts. However, previous approaches focus on the text encoder, leaving the potential of learnable prompts within the audio encoder unexplored. In this paper, we propose a novel framework that introduces trainable prompts into the audio encoder to capture task-specific acoustic features. We demonstrate that integrating audio-side prompt learning with existing text-side approaches enhances few-shot adaptation. Through extensive experiments across 11 datasets show that integrating our...


## Candidate 046

Query: personalized recommendation with large language models

Likely paper IDs:

1. `2606.20554v1` score=0.3821
   Title: Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
   Categories: cs.IR, cs.AI
   Abstract: Generative recommendation is an emerging paradigm that has shown promise in industrial recommendation systems, aiming to predict users' next interactions from their historical behaviors. At the core of generative recommendation lies item tokenization, which bridges item semantics and recommendation models. However, existing methods often struggle to effectively organize and inject complex user-behavioral and item-semantic contexts into recommendation models simultaneously. On the one hand, existing graph-based integration methods, such as graph serialization and graph neural networks, either suffer from scalability issues or exploit only local graph information. On the other hand, existing s...

2. `2606.10357v1` score=0.2988
   Title: Atomic Intent Reasoning: Bringing LLM Semantics to Industrial Cross-Domain Recommendations
   Categories: cs.IR, cs.AI
   Abstract: Cross-domain recommendation is a core problem in content-to-e-commerce platforms. Its objective is to leverage user interactions with content to infer potential purchasing intent on the e-commerce side, thereby enhancing conversion rates and commercial value. However, in real industrial scenarios, cross-domain recommendation faces multiple challenges: significant semantic gaps exist between different domains, and user cross-domain behavior sequences are often massive in scale and rich in noise. Although large language models (LLMs) possess powerful semantic understanding and reasoning capabilities, their millisecond-level inference latency makes direct application in online recommendation sy...

3. `2606.19635v1` score=0.2929
   Title: Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
   Categories: cs.IR, cs.AI, cs.LG
   Abstract: Large Recommendation Models (LRMs) have demonstrated promising capabilities in industry-scale recommendation tasks. However, holistically integrating traditional signals into these transformer-based architectures effectively and efficiently remains a major challenge. Conventional approaches that "textualize" these signals directly or create discrete item representations often lead to excessively long prompts, substantial memory footprints, and high computational overhead. To overcome these limitations, we propose "Token Factory", a framework designed to transform traditional signals into "soft tokens" that can be directly processed by LRMs. This approach enables efficient integration and com...

4. `2606.14260v1` score=0.2870
   Title: ChronoID: Infusing Explicit Temporal Signals into Semantic IDs for Generative Recommendation
   Categories: cs.IR, cs.AI
   Abstract: Semantic IDs are crucial in generative recommendation, but with a fundamental limitation: temporal information is not well incorporated into semantic IDs. Instead, time influences recommendation only implicitly (e.g., through session construction heuristics, preference alignment, or sequence order), while existing semantic ID learning remains entirely time-agnostic. This design conflates interactions occurring under distinct temporal contexts into identical semantic representations, implicitly assuming that item semantics and user intent are temporally stationary. Such an assumption is misaligned with real-world recommendation scenarios, where evolving interaction rhythms play a central role...

5. `2606.09038v1` score=0.2798
   Title: Personalization Meets Safety:Mechanisms,Risks,and Mitigations in Personalized LLMs
   Categories: cs.AI
   Abstract: Large Language Models (LLMs) have enabled increasingly personalized interactions by adapting to users' preferences, contexts, and long-term histories. However, the mechanisms that enable personalization also expand the safety landscape in ways not systematically addressed by existing literature. Existing reviews typically focus either on personalization or safety, leaving their intersection largely unexplored. We present the first comprehensive, safety-aware review of personalized LLMs. We organize personalization along three dimensions-user representation, personalization paradigm, and evaluation-and introduce a unified taxonomy of safety risks. At the representation level, we analyze risks...

6. `2606.18897v1` score=0.2329
   Title: SAERec: Constructing Fine-grained Interpretable Intents Priors via Sparse Autoencoders for Recommendation
   Categories: cs.IR, cs.AI
   Abstract: Intent-based recommender systems have gained significant attention for improving accuracy and interpretability by modeling the underlying motivations behind user behaviors. Most existing models derive intents directly from user sequences via clustering or prototype learning. However, they are sensitive to sequence quality, require presetting the number of intents, and lack explicit semantic grounding. These issues lead to an incomplete and coarse intent set and limit the effectiveness of recommendation. In this paper, we propose the Sparse Autoencoder for intent-based recommendation (SAERec), a novel recommender that automatically constructs a fine-grained and interpretable intent space from...

7. `2606.10120v2` score=0.2277
   Title: MetaPlate: Counterfactual-Guided RAG-LLM Tool for Personalized Food Recommendation and Hyperglycemia Prevention
   Categories: cs.IR, cs.AI, cs.HC
   Abstract: Postprandial hyperglycemia is a key risk factor for metabolic disorders; however, existing dietary guidance is often static, impractical, and insufficiently personalized, providing recommendations that are difficult to follow or not impactful. While recent advances leverage continuous glucose monitoring (CGM) and machine learning to predict glycemic responses, these approaches are largely predictive and lack actionable guidance. Moreover, recommendation systems are often misaligned with user goals and require extensive input. We present MetaPlate, a counterfactual explanation (CF) guided, context-aware decision-support framework that generates personalized meal recommendations to mitigate po...

8. `2606.15331v1` score=0.2036
   Title: HoloRec: Holistic Encoding and Interleaved Reasoning for Generative Recommendation
   Categories: cs.IR, cs.AI
   Abstract: Generative recommendation models that formulate the task as sequence generation overcome the objective fragmentation problem of traditional cascade architectures, yet existing approaches still suffer from flat semantic representations lacking hierarchical structure for multi-step reasoning and an externally constructed chain-of-thought (CoT) that requires expensive annotations and remains disconnected from the generation objective. We propose HoloRec, an endogenous chain-of-thought recommendation mechanism that unifies representation, reasoning, and generation by constructing a hierarchical semantic encoding matrix via multi-granularity nested residual quantization optimized by a holistic re...


## Candidate 047

Query: neural information retrieval reranking

Likely paper IDs:

1. `2606.11945v1` score=0.3981
   Title: uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking
   Categories: cs.CL, cs.IR
   Abstract: This report describes our participation in SemEval-2026 Task 8 on multi-turn retrieval and question answering. The task evaluates conversational systems across four domains (finance, cloud documentation, government, Wikipedia), and includes unanswerable queries where the available collection does not contain sufficient evidence to produce a complete response. We propose a multi-turn retrieval-augmented generation pipeline that combines learned sparse retrieval with LLM-based reranking and generation. Using sparse retrieval as the primary retrieval method, we leverage its strong generalization across domains. In addition, we make use of the long-context capabilities of LLMs for conversational...

2. `2606.11265v1` score=0.3438
   Title: When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines
   Categories: cs.CR, cs.AI
   Abstract: Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection. Existing studies mainly evaluate poisoning under simplified retrieval settings, overlooking practical RAG pipelines involving document chunking, dense retrieval, reranking, and grounded generation. In this paper, we revisit corpus poisoning under realistic multi-stage retrieval pipelines and show that many existing attacks substantially degrade after reranking despite achieving high retrieval-stage relevance. We identify retrieval granularity mismatch as a key reason for this failure: document-level adversarial signals are oft...

3. `2606.07924v1` score=0.2093
   Title: Decoupling Semantics and Logic: A Training-Free Coarse-to-Fine Pipeline for Video Retrieval-Augmented Generation
   Categories: cs.CV, cs.AI, cs.CL, cs.LG, cs.MM
   Abstract: This paper presents our system description for the 2nd Workshop on Multimodal Augmented Generation via MultimodAl Retrieval (MAGMaR). Addressing the critical challenges of cross-lingual long-video comprehension, strict persona adherence, and zero-hallucination temporal grounding, we propose a fully training-free, two-stage cascaded Video RAG pipeline. Our architecture strategically decouples semantic retrieval from cognitive logical reasoning through a modality-aware division of labor. In the first stage, a high-recall semantic pre-fetching module employs dense retrieval using only high-fidelity visual summaries and global text descriptions, explicitly isolating noisy modalities (e.g., OCR a...

4. `2606.15741v1` score=0.2079
   Title: A Self Consistency Based Reranking for Narrative Question Answering
   Categories: cs.CL, cs.AI
   Abstract: Narrative question answering (NQA) is a challenging task in natural language processing that requires models to understand long textual contexts, capture relationships across events, and generate coherent responses. Despite recent advances in pretrained language models, most existing approaches rely on a single decoding output during inference, making them sensitive to generation variability and often resulting in incomplete or inconsistent answers .To address this limitation, we propose a self-ensemble Self-Consistency-Based reranking framework for narrative question answering. The proposed method generates multiple candidate answers for each story-question pair and selects the final answer...

5. `2606.12294v1` score=0.1839
   Title: Bridging the Modality Gap in Forensic Image Retrieval
   Categories: cs.CV, eess.IV
   Abstract: Automated image retrieval plays an increasingly critical role in modern forensic analysis, supporting investigative workflows that rely on efficient comparison of visual evidence. While prior work has focused primarily on developing and optimizing multimodal retrieval systems, limited attention has been paid to evaluating the forensic applicability of these technologies across diverse real-world scenarios. In this study, we present a unified retrieval framework adapted to four key forensic tasks: (1) tattoo image retrieval given a tattoo query image; (2) tattoo retrieval guided by human-expert textual descriptions, modelling the common situation where a witness verbally describes a tattoo; (...

6. `2606.17910v1` score=0.1834
   Title: Non-negative Elastic Net Decoding for Information Retrieval
   Categories: cs.IR, cs.AI, cs.CL
   Abstract: Dense retrieval has become the dominant paradigm in information retrieval, in which each document is scored against a query by the inner product of their vector embeddings, and the top-$k$ documents by score are retrieved for this query. However, since each document's score depends solely on the embedding of the query and itself, the retrieval process is oblivious to the content of the entire corpus. Therefore, dense retrieval cannot avoid selecting semantically similar documents from the corpus, which may result in a non-diverse, redundant set of retrieved documents. To this end, we approach retrieval as a joint decoding problem, in which documents are selected as a set with regard to the c...

7. `2606.14269v1` score=0.1700
   Title: ScoreGate: Adaptive Chunk Selection for Retrieval-Augmented Generation via Dual-Score Statistical Fusion
   Categories: cs.IR, cs.CL
   Abstract: Fixed-cardinality retrieval injects a constant top-K chunks into the generator regardless of query complexity, causing over-retrieval for narrow queries and under-retrieval for compositional ones. We describe ScoreGate, a lightweight score-space decision mechanism that controls retrieval cardinality at inference time using two scores already produced by the standard pipeline: bi-encoder similarity s_i and cross-encoder reranker score r_i, with no additional model inference calls required. Its core insight is that cross-encoder affirmation can rescue semantically relevant chunks that bi-encoder retrieval ranks poorly due to vocabulary mismatch -- a failure mode unaddressed by fixed-K or singl...

8. `2606.07783v1` score=0.1577
   Title: Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval
   Categories: cs.CL
   Abstract: Retrieval-Augmented Generation (RAG) is widely used to improve the factual reliability of large language models (LLMs) by grounding answers in retrieved evidence. In misinformation-rich environments, however, retrieved content may include plausible but incorrect information, raising concerns about the reliability of RAG-based information access systems. In this work, we propose an evaluation protocol to systematically test how the RAG system handles conflicts between parametric knowledge and evidence retrieved from context with varying amounts of misleading information. We target correct answers to factoid questions that the model responds to correctly, even when there is no retrieval, and u...


## Candidate 048

Query: benchmark for agentic AI systems

Likely paper IDs:

1. `2606.14816v1` score=0.3378
   Title: A Security Analysis of Long-Horizon Agentic AI Systems: Threats, Evaluation, and Framework Development
   Categories: cs.CR, cs.AI
   Abstract: This paper presents a structured analysis of security challenges in long-horizon agentic AI systems. The study reviews existing threats, evaluation approaches, attack propagation mechanisms, and security frameworks. A taxonomy of security threats and a framework for analyzing attack propagation are proposed to support future research in agentic AI security

2. `2606.16649v1` score=0.3375
   Title: The Integrator Advantage: Controlled Agentic AI for Small and Medium-Sized Companies
   Categories: cs.AI
   Abstract: Agentic AI marks a new phase of enterprise automation. Unlike traditional automation or conversational AI, agentic systems can interpret goals, plan multi step tasks, access tools, interact with enterprise systems, and execute workflows with varying degrees of autonomy. For small and medium sized companies, this creates potential to reduce administrative burden, accelerate routine processes, and improve the use of organizational knowledge. This paper argues that the near term value of Agentic AI does not lie in full autonomy or workforce reduction, but in controlled partial autonomy for simple and medium complexity business processes. It proposes an integration framework covering use case su...

3. `2606.19899v1` score=0.3374
   Title: Measuring Biological Capabilities and Risks of AI Agents
   Categories: cs.CY, cs.AI
   Abstract: This paper addresses a rapidly emerging policy challenge: how to generate and interpret credible evidence about the biological capabilities and risks of AI scientists, or agentic AI systems capable of autonomously or collaboratively performing multi-step scientific tasks. As these systems enter real research workflows, decision-makers increasingly face evaluation results whose meaning depends on underlying design choices that are often implicit or under-documented. We synthesize current evidence on AI-enabled biological risks and introduce biological agentic evaluations as a promising, but interpretation-sensitive, tool for assessing these systems. Our central contribution is a set of practi...

4. `2606.15485v1` score=0.3337
   Title: The Perils of Agency: How Developers Perceive, Prioritize, and Address Risks in Agentic AI Products
   Categories: cs.CY, cs.AI, cs.HC, cs.LG, cs.SE
   Abstract: Agentic AI systems act autonomously, use tools, adapt to context, and operate in complex real-world environments. However, these same characteristics can create or exacerbate product risks. We studied how industry developers (n=35) perceive, prioritize, and address the risks in their agentic AI products. We found that developers' perceptions of risk were closely tied to the qualities that made the product agentic, such as autonomy, tool use, and usage in a real-world context. Developers prioritized product and business risks before considering downstream societal risks like job displacement and end-user privacy. This prioritization also impacted developers' ability and motivation to mitigate...

5. `2606.11769v1` score=0.2748
   Title: When Do Data-Driven Systems Exhibit the Capability to Infer?
   Categories: cs.AI, cs.LG
   Abstract: The European AI Act is the first comprehensive regulation of artificial intelligence (AI), setting out extensive obligations, particularly for so-called high-risk and general-purpose AI systems. A key distinguishing feature of AI systems under the AI Act is the capability to infer. Since the AI Act does not clearly define what inference is, there is a gray area for certain data-driven systems. A specific example is credit scoring systems, which are listed by Annex III of the AI Act. At the same time, however, these are often implemented using statistical models for which it is unclear whether they have the capability to infer and thus fall under the AI definition of the AI Act at all. Motiva...

6. `2606.07812v1` score=0.2655
   Title: Scaling Participation in Modular AI Systems
   Categories: cs.AI, cs.CL
   Abstract: Humanity is a mosaic of multifaceted talents and needs, and any truly intelligent AI must reflect that richness. Yet the LLMs used by all are built by the few -- a centralized market of monolithic AI models structurally ill-suited to capture the diversity of human knowledge, reasoning, and values. Here we introduce scaling participation, a new paradigm in which modular AI systems are built from the bottom up through the contributions of diverse stakeholders. Participants contribute small models trained on their own interests and priorities; these models then collaborate in modular frameworks as compositional AI systems. Participatory AI systems outperform monolithic LLMs by up to 15.4% acros...

7. `2606.11533v1` score=0.2535
   Title: AI Researchers Must Help Lead Arms Control to Mitigate Military AI Risks
   Categories: cs.CY, cs.AI, cs.ET, cs.LG
   Abstract: The advancement of AI capabilities compels researchers and the public to be more aware of its potential worldwide impact. A pressing near-term concern is the regulation of military AI applications. Armament manufacturers and defense contractors are increasingly investing in AI capabilities and forging partnerships with AI companies, creating a burgeoning coalition that demands military leaders, arms control diplomacy experts, and AI researchers collaborate to ensure a safer future. While AI researchers often focus on the long-term implications of superintelligent AI, this approach may not adequately address the immediate challenges posed by AI in military applications. Success requires ackno...

8. `2606.12835v1` score=0.2506
   Title: The Internet of Agentic AI: Communication, Coordination, and Collective Intelligence at Scale
   Categories: cs.MA, cs.AI, cs.CY, cs.NI
   Abstract: The rapid emergence of autonomous AI agents is transforming artificial intelligence from isolated model inference into distributed systems of reasoning, communication, and action. This paper develops the vision of the Internet of Agentic AI (IoAI): an open ecosystem in which heterogeneous agents discover one another, negotiate responsibilities, exchange context, invoke tools, and execute workflows across cloud, edge, device, organizational, and cyber-physical environments. We synthesize foundations from single-agent agentic AI, multi-agent systems, distributed computing, communication networks, game theory, and security engineering to characterize the architectures and mechanisms required fo...


## Candidate 049

Query: efficient inference for large language models

Likely paper IDs:

1. `2606.11906v1` score=0.2091
   Title: When Does Language Matter? Multilingual Instructions Reveal Step-wise Language Sensitivity in Vision-Language-Action Models
   Categories: cs.CL
   Abstract: Vision-Language-Action (VLA) models have shown strong performance in language-conditioned robotic manipulation, yet their robustness to linguistic variation remains poorly understood. In this work, we present the first systematic multilingual evaluation of VLA models by translating the LIBERO benchmark into ten languages, revealing severe performance degradation under non-English instructions, with success rates dropping by 30-50%. Through fine-grained analysis of task executions, we find that language influence is highly non-uniform across steps: certain steps exhibit strong language dependence and dominate overall task failure, while others are largely language-agnostic. Based on this insi...

2. `2606.17820v1` score=0.2036
   Title: Improving low-resource ASR using bilingual fine-tuning with language identification: a cross-linguistic evaluation
   Categories: cs.CL
   Abstract: This study explores how bilingual fine-tuning affects automatic speech recognition (ASR) in low-resource languages. We evaluate this method across nine linguistically and geographically diverse language pairs, covering a range of language families and writing systems. To distinguish the two languages, during training, we pre-pend each input text with a language identification token. At inference, the model jointly predicts both the language and transcription from the speech input alone. As texts for which the language is incorrectly determined show low ASR performance, we also conduct a follow-up experiment in which the language identification token is provided both during training and infer...

3. `2606.19264v1` score=0.1982
   Title: Structured Inference with Large Language Gibbs
   Categories: cs.LG, cs.CL
   Abstract: The knowledge encoded in large language models (LLMs) can serve as a substrate for structured reasoning over variables describing a complex world, but accessing this knowledge in a probabilistically coherent manner poses a difficult inference problem. We propose Large Language Gibbs, a scheme for structured probabilistic inference that uses conditional distributions of an LLM as transition operators. Rather than sampling structured objects through single-pass autoregressive generation, we iteratively resample individual variables conditioned on others using an LLM's next-token conditionals. This approach avoids order-dependent biases and produces a stationary distribution that reflects a com...

4. `2606.08684v1` score=0.1961
   Title: BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving
   Categories: cs.CV
   Abstract: We present BLUE, a minimal method for better language use in vision-language-action (VLA) models for autonomous driving (AD). Through extensive analysis, we reveal that language matters on only a small fraction of routes, but on those routes it can greatly improve or degrade performance. Generating language at every frame is therefore inefficient, since most computation is spent on frames that do not benefit from language. We further show that pretrained VLA hidden states potentially already encode whether language will benefit a given frame, even though scene complexity and kinematic features alone struggle to predict this. Based on this finding, BLUE trains a lightweight gate on frozen VLA...

5. `2606.19475v1` score=0.1824
   Title: Diffusion Language Models: An Experimental Analysis
   Categories: cs.AI, cs.CL
   Abstract: Large Language Models (LLMs) have revolutionized language modeling through autoregressive generation, enabling strong performance across a wide range of tasks. Recently, Diffusion Language Models (DLMs) have emerged as an alternative paradigm that generates text through iterative denoising rather than next-token prediction, allowing parallel refinement of entire sequences. While numerous diffusion-based architectures have been proposed, differences in evaluation protocols, datasets, inference budgets, and generation hyperparameters make it difficult to compare their capabilities and understand the trade-offs they offer. In this work, we present a systematic experimental analysis of modern DL...

6. `2606.19584v1` score=0.1776
   Title: Language-Instructed Vision Embeddings for Controllable and Generalizable Perception
   Categories: cs.CV
   Abstract: Vision foundation models are typically trained as static feature extractors, placing the burden of task adaptation onto large downstream models. We propose an alternative paradigm: instead of solely feeding visual features into language models, we use language itself to dynamically guide the vision encoder. Our method, Language-Instructed Vision Embeddings (LIVE), leverages language as high-level guidance to produce task-centric embeddings at inference time, removing the need for task-specific retraining. This enables the encoder to focus on contextually relevant aspects of the input, yielding more controllable and generalizable representations. Empirically, LIVE reduces visual hallucination...

7. `2606.08994v1` score=0.1721
   Title: Language-Aware Token Boosting: LLM Language Confusion Reduction Without Tuning
   Categories: cs.CL
   Abstract: Large language models (LLMs) sometimes exhibit language confusion when generating non-English text. Existing approaches typically rely on fine-tuning to mitigate this issue. In contrast, we propose a tuning-free paradigm for reducing language confusion. Within this paradigm, we introduce two methods: Language-Aware Token Boosting (LATB), which applies targeted perturbations to tokens associated with the desired language, and Adaptive Language-Aware Token Boosting (Adaptive-LATB), which dynamically adjusts these perturbations based on the model's confidence in the intended language. Experiments demonstrate that our methods effectively improve multilingual alignment by reducing language confus...

8. `2606.19534v1` score=0.1718
   Title: PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models
   Categories: cs.CV, cs.AI, cs.CL
   Abstract: Multimodal large language models (MLLMs) have achieved remarkable progress in visual understanding tasks. However, most existing MLLMs rely on autoregressive generation, which limits their efficiency for perception tasks that require captioning multiple regions. In this work, we propose PerceptionDLM, a multimodal diffusion language model optimized for efficient parallel region perception. Built upon PerceptionDLM-Base, a strong foundational baseline that achieves state-of-the-art performance among open-source diffusion MLLMs, our architecture fully leverages the parallel decoding nature of DLMs. Specifically, we introduce efficient prompting and structured attention masking to enable simult...


## Candidate 050

Query: quantization of neural networks

Likely paper IDs:

1. `2606.10520v1` score=0.4285
   Title: UniSVQ: 2-bit Unified Scalar-Vector Quantization
   Categories: cs.CL
   Abstract: Post-training quantization at the 2-bit level enables low-cost deployment and inference acceleration for large language models (LLMs). Scalar quantization (SQ) and vector quantization (VQ) are two primary quantization methods, however, the former suffers from significant performance degradation, and the latter incurs computational and storage overhead. We propose UniSVQ, a unified 2-bit quantization framework that bridges scalar and vector quantization by parameterizing codewords as an affine transform of integer lattices. This structure preserves compatibility with optimized integer kernels while retaining much of VQ's flexibility. We further introduce a data-driven block-wise fine-tuning s...

2. `2606.07819v1` score=0.4157
   Title: Joint Structural Pruning and Mixed-Precision Quantization for LLM Compression
   Categories: cs.AI, cs.LG
   Abstract: Recently, the efficiency of Large Language Models (LLMs) deployment has become a critical concern in practical applications. While post-training quantization (PTQ) and structural pruning are established techniques for reducing memory footprint and inference latency, most existing PTQ approaches optimize quantization errors on a per-layer basis, overlooking how errors accumulate and propagate through the network, often resulting in suboptimal solutions. Traditional pipelines also tend to apply pruning and quantization in isolation or sequentially, further compounding sub-optimality. We introduce a novel end-to-end framework that addresses these limitations in two key ways. First, we propose a...

3. `2606.10890v1` score=0.3582
   Title: Optimal Post-Training Quantization Scales and Where to Find Them
   Categories: cs.LG, cs.AI
   Abstract: Post-training quantization (PTQ) compresses large language models by mapping weights to low-bit representations. The scaling factor that defines the quantization grid is typically chosen using simple, data-free heuristics. In this work, we present PiSO (Piecewise Scale Optimization), an algorithm that leverages calibration data to compute the optimal channel-wise weight scales exactly and efficiently under round-to-nearest quantization. PiSO partitions the scale search space into finitely many intervals on which the objective admits a closed-form minimizer. We extend PiSO to group-wise quantization via principled heuristics and propose effective strategies for interleaving scale optimization...

4. `2606.13300v3` score=0.3483
   Title: Quantizing Time-Series Models As Dynamical Systems: Trajectory-Based Quantization Sensitivity Score
   Categories: cs.LG
   Abstract: We introduce the Trajectory-based Quantization Sensitivity Score (TQS), a metric that reframes post-training quantization (PTQ) through the lens of dynamical-systems stability. By modeling the network's rollout as a discrete-time dynamical system, TQS characterizes how quantization-induced errors propagate and amplify over the rollout horizon. Unlike conventional PTQ methods, where sensitivity analysis is often coupled to the quantization procedure, TQS enables a priori sensitivity estimation decoupled from quantizer selection and bit-width assignment. This separation allows for quantization budget planning even for black-box or compiled networks with fused operators. Building on this, we pr...

5. `2606.12487v1` score=0.3333
   Title: DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics
   Categories: cs.LG
   Abstract: Post-training quantization (PTQ) is essential for efficient large language model inference, but reliably quantizing activations remains challenging when weights, activations, and KV caches are all quantized to 4-bit precision. A key difficulty lies in massive activations, whose extreme values dominate the activation range and amplify quantization errors. State-of-the-art methods mainly mitigate massive activations through transformation-based smoothing, such as orthogonal rotations and affine scaling, but overlook the cross-layer dynamics of the residual stream. In this paper, we show that massive activations emerge and disappear in a phase-wise pattern across network depth, triggering large...

6. `2606.15523v1` score=0.3327
   Title: AQ4SViT: An Automated Quantization Framework with Search Gating Policy for Compressing Spiking Vision Transformers
   Categories: cs.NE, cs.AI, cs.LG
   Abstract: Spiking Vision Transformers (SViTs) have emerged as alternative low-power ViT models, but their large sizes hinder their deployments on resource-constrained embedded AI systems. To address this, state-of-the-art works proposed quantization techniques to compress SViT models, but their manual, human-guided approach needs a huge design time and power/energy consumption to find the appropriate quantization setting for each given network, making this approach not scalable for quantizing multiple networks. Toward this, we propose AQ4SViT, a novel automated quantization framework for SViTs that can provide quick quantization settings with good trade-offs between accuracy and memory. To achieve thi...

7. `2606.09927v1` score=0.2997
   Title: Trainable Smooth-Rotation Transforms with Learned Channel Scales for LLM Quantization
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: Post-training quantization (PTQ) is one of the most practical ways to reduce the serving cost of Large Language Models (LLMs), but activation quantization remains difficult because outlier-dominated channels lead to large quantization errors. This paper investigates whether part of this degradation is caused by over-migration in scaling-based equivalent transformations. We introduce a quantile-robust scaling policy for SmoothRot-style transforms by replacing max-based activation statistics with high quantiles, and we complement it with constrained gradient-based optimization of channel scales. On LLaMA-3.2-1B under W4A4 quantization, quantile-only policy search improves selected-layer error ...

8. `2606.07116v1` score=0.2886
   Title: OffQ: Taming Structured Outliers in LLM Quantization by Offsetting
   Categories: cs.LG, cs.AI, cs.CL
   Abstract: Low-bit quantization has been widely adopted to accelerate the inference of large language models (LLMs) by significantly reducing computational cost and memory usage. However, activation outliers pose a major challenge to effective quantization, often leading to notable performance degradation. In this paper, we introduce OffQ, a method designed to mitigate activation outliers in low-bit quantization through a novel offsetting mechanism. Specifically, OffQ first identifies a low-dimensional outlier subspace in the activations using a proposed top-1 PCA, and then concentrates high-magnitude activations into 1 channel via rotation. OffQ then absorbs this concentrated outlier channel by conver...

