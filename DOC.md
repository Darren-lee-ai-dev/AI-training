# Project Summit — Instructions

Source: saved Project Summit page (October 15, 2026).

## Instructions

How to write a question that passes the checks.

## Overview

You're helping build a sample of graduate/PhD-level questions in your specific field. These samples will be used to probe the frontier of expert knowledge — questions a PhD in your field should be able to solve, but which today's strongest AI model gets right only some of the time.

Your job is to write one graduate/PhD-level question with a self-made image, a closed-ended answer, a detailed step-by-step solution, and a grading rubric. After you submit, Summit's automated checks test the question's quality and whether frontier AI models can solve it.

Create and submit the question in Summit. There are no automated checks to run before you submit: Summit's quality and difficulty checks run after submission, and a question they flag comes back to you with written reasons. Treat this page and the in-product checklist as your quality gate.



## Quality bar (read this first)

### Overview

We prioritize quality over quantity. A single excellent submission is worth more than five mediocre ones. If we cannot guarantee quality to our client, the project ends. Concretely:

### Graduate/PhD-level only

"Graduate-level" means the average person with a graduate degree in your subfield could solve it; the average person without one could not. If the content is taught in standard undergraduate courses (e.g., introductory organic chemistry, calculus, classical mechanics, general biology, standard algorithms and data structures, an introductory machine-learning course, circuit analysis, statics), it does not qualify, even if the calculation is long.

- **Too easy:** "Determine the hybridisation of the labeled carbon"
- **At the bar:** "Using Bent's rule, rank the s-character of the three C-C bonds at the bridgehead of the strained cage shown, and give the bond the largest s-character"

### Difficulty target

After you submit, Claude Opus 5.5 (high reasoning effort) attempts your question 5 times, independently. Your question is accepted only if it answers correctly on **1 to 4** of the 5 attempts.

- **5 of 5 correct:** too easy. It comes back to you to make harder.
- **0 of 5 correct:** too hard, or possibly a wrong answer key. It comes back to you to check.
- A weaker AI model, Claude Sonnet 5.5, also gets 3 attempts. If it solves the question on 2 or more of them, it comes back to you as too easy and for you to make it harder.

Difficulty must come from the reasoning, not from the length of the calculation. Bigger numbers, more algebra or more steps of the same kind do not make a question harder: the model either grinds through them reliably, or runs out of room and never answers. Neither measures what we want. The best questions have a step where the natural approach gives a plausible but wrong answer.

The same applies to code: if a short program, a simulation or a brute-force search gives the answer, the question is too easy. Code in a solution is fine for evaluating or checking results you've already derived, but the reasoning must be in the written steps.

### One question, one answer

No compound questions ("compute X and Y"). No open-ended prompts ("explain why," "discuss," "provide a theory"). No subjective interpretation. The answer must be a single, objectively correct, unambiguous value, expression, or short string.

- **Wrong:** "Find the ground-state energy and sketch the wavefunction and comment on degeneracy"
- **At the bar:** "Give the first-order correction to the ground-state energy, in units of lambda/L"

If the same answer can be written in more than one form (e.g. an exact fraction and its decimal), list the other forms in **Also accepted**. If the question genuinely has more than one different correct answer, rewrite it so it has exactly one.

### Non-searchable

A determined searcher with Google, Wikipedia, and the standard textbook should not be able to find the answer in under 5 minutes. Build questions on top of recent research, niche specializations, multi-step synthesis of disparate facts, or your own research experience — not facts that exist verbatim on a webpage.

### Stable answers

The answer must not change over time or depend on the setup used to check it.

- No questions about benchmark scores, the behaviour of specific AI models, or results that only appear in very recent papers. These go out of date and are often findable.
- No answers that depend on a programming language or library version, compiler, hardware or random seed. If the question includes code, state the language and version.
- In engineering, give every material property, coefficient and table value the question needs. Do not rely on a design code or handbook (ASME, IEEE, Eurocode, etc.) for values you don't quote.

### Original work

Your own creation or a non-trivial synthesis of published material. No copying from textbooks, problem sets, exams, or online sources. Lightly reworded problems will be rejected.

### No prohibited content

No weapons of mass destruction (CBRN). No content requiring subjective or moral interpretation.

### Closed-ended and gradable

The answer must be checkable by comparing a string or a number. If grading it would require human judgement of an essay, it is out of scope.

### The Text-only

Text-only submissions are allowed only when the stem stands alone and only within Summit's soft per-category no-image allowance. Prefer a necessary image whenever the domain calls for one.

## Submission components

### Overview

The Summit submission workspace asks for each of the following.

### Flow

1. Pick one of your assigned subject domains and a specific sub-topic.
2. Draft the question and answer key in Summit.
3. Create the image yourself and upload a clean PNG or PDF when the question requires one.
4. Write the numbered step-by-step solution with every formula and unit shown.
5. Write the grading rubric.
6. Complete every required submission field and submit.
7. If the automated checks or a reviewer return the question, fix what they name and submit again.

### Importing from a zip (optional)

Instead of typing every field, you can fill the form from a zip file: press **Import .zip** on the Submit page.

- Importing only fills the form. Check every section, then press **Submit** yourself.
- Everything on this page still applies to imported content, and every automated check runs after you submit.
- The domain must be one of your assigned domains. If it isn't, Summit switches it to an assigned domain and warns you; check it before submitting.
- If the rubric in the zip can't be read, the rubric starts empty. Write it again before submitting.

**Zip layout.** Put the files at the top level of the zip. Zip the files themselves, not a folder that contains them.

```
my-question.zip
├── task.json        required
├── image.png        optional: image.png | image.jpg | image.jpeg | image.webp | image.gif  (max 5 MB)
└── reference.pdf    optional: reference.pdf | .png | .jpg | .jpeg | .webp | .txt         (max 10 MB)
```

Files with any other name are ignored.

**task.json:**

```
{
  "schema_version": "summit-task-package-v1",
  "task": {
    "domain": "mathematics",
    "subdomain": "Group theory",
    "modality": "image_reference",
    "taskType": "image_multistep_discrete_reasoning",
    "imageCreationTool": "TikZ",
    "imageNecessityExplanation": "Why the question cannot be answered without the image.",
    "questionText": "Full question stem.",
    "answerType": "exact_match",
    "finalAnswer": ["42"],
    "acceptableAnswerVariants": ["forty-two"],
    "multipleChoiceOptions": [],
    "answerPrecision": { "kind": "none" },

    "solution": "Step-by-step reasoning to the answer key.",
    "references": "Author, Title, Journal (year).",

    "rubric": {
      "criteria": [
        { "id": "c1", "description": "Gives the final answer 42.", "points": 5, "isFinalAnswer": true },
        { "id": "c2", "description": "First key reasoning step.", "points": 3, "isFinalAnswer": false },
        { "id": "c3", "description": "Second key reasoning step.", "points": 2, "isFinalAnswer": false }
      ],
      "commonWrongAnswers": ["36"]
    },

    "image": { "entry": "image.png" },
    "referenceFile": { "entry": "reference.pdf", "fileName": "source.pdf" }
  }
}
```

**Allowed values:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Field Values|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `schema_version` Exactly `summit-task-package-v1`| `domain` `mathematics`, `physics`, `chemistry`, `biology_medicine`, `computer_science_ai`, `engineering`, `humanities_social_science`, `other` (must be one of your assigned domains)| `modality` `image_reference` or `text_only` (for `text_only`, leave out `image`)| `taskType` `image_quantitative_derivation`, `image_classification_identification`, `image_multistep_discrete_reasoning`, `graph_extraction_computation`, `other_admin_approved`, or `not_applicable` for text-only questions| `answerType` `exact_match` or `multiple_choice`| `answerPrecision` `{ "kind": "none" }`, `{ "kind": "significant_figures", "digits": 3 }` or `{ "kind": "decimal_places", "digits": 2 }` | | | | | | | | | | | | | |

**Rules:**

- **Exact match:** put the answer key in `finalAnswer`, and equivalent forms in `acceptableAnswerVariants`.
- **Multiple choice:** give 5 to 12 `multipleChoiceOptions`, with the **correct option first**. `finalAnswer` is not used.
- **Precision:** if the question asks for a precision, set `answerPrecision` to match it.
- **Rubric:** 3 to 5 criteria; points add up to exactly 10; exactly one criterion has `"isFinalAnswer": true`, and it states the answer key; none of the `commonWrongAnswers` may be the answer key.
- **Length limits:** question up to 20,000 characters, solution up to 30,000, each answer up to 5,000.

### 1. Subject domain

One of your assigned domains: Mathematics, Physics, Chemistry, Biology/Medicine, Computer Science/AI, or Engineering.

### 2. Subject sub-topic

The specific subfield (e.g., "Quantum Field Theory," "Asymmetric Organic Synthesis," "Algebraic Topology," "Structural Biology," "Computational Complexity," "Reinforcement Learning Theory," "Control Systems," "Power Electronics"). Choose something where your own expertise is load-bearing.

### 3. The question

The full question text, including all assumptions, given values, and definitions of any non-standard terms or notation. The question must be non-searchable. After reading the question alone (plus the image), a domain expert should know exactly what is being asked.

**Formatting rules:**

- Write mathematical content, symbols, equations, units, and chemical formulas in LaTeX (e.g., `$\Delta G^\circ = -RT \ln K$`) and verify the rendered preview.
- Put code and pseudocode in code blocks, as text. Never as a screenshot.
- Precise technical language. A single ambiguous word can change the answer; choose carefully.
- State all assumptions in the question itself. Do not bury them in the solution. (e.g., "Assume ideal gas" or "neglect spin-orbit coupling")
- If the answer is numeric, state the precision you want in the question (e.g. "to three significant figures"). Grading is strict at the precision the question asks for.
- If the answer is an asymptotic bound, say which notation (Θ, O or Ω) and form you want (e.g. "give a tight bound in Θ notation, in simplest form").
- If you use non-standard jargon, define it. Or don't use it at all.
- Reference the image explicitly ("In the diagram below…" or "Using the structure shown…").


**Per-domain:**

- **Chemistry:** ChemDraw for structures/mechanisms; show stereochemistry explicitly; label every atom the question refers to.
- **Physics:** TikZ or Python for circuits, potentials, and geometries; mark coordinate axes, signs and directions; give scales.
- **Biology:** BioRender or PyMOL for pathways/structures; label nodes, edges and directions; if it is a tree, show branch calibration.
- **Mathematics:** TikZ/Asymptote or Desmos for graphs, knots, complexes; label all vertices, orientations and marked points.
- **Computer Science/AI:** TikZ or Graphviz for graphs, automata, trees and network architectures; label every node, edge weight, state and layer dimension the question uses.
- **Engineering:** CircuiTikZ or KiCad for circuits; TikZ, MATLAB/Simulink or CAD for block diagrams, free-body diagrams and drawings; mark units, scales, directions and tolerances.

### 5. Final answer

The exact answer, with no surrounding prose.

- **Bad:** The free energy change is approximately -42.3 kJ/mol, which is favorable.
- **Good:** `-42.3 kJ/mol`

LaTeX for any non-text content. Give the answer at the precision the question asks for. Prefer exact forms (fractions, surds, closed-form expressions) where the question allows them. Use SI units unless the field convention requires otherwise (state which). One answer only — pick the canonical form, and list any equivalent forms in **Also accepted (optional)** so they are graded as correct.

Two answer formats are allowed:

- **Exact-match:** a single number, expression, or short string.
- **Multiple-choice:** five or more options, exactly one correct.

### 6. Step-by-step solution

A complete, sequential derivation showing how to arrive at the answer. Format it as numbered steps:

```
Step 1: [What this step does, one line]
[Equations, reasoning, calculations]

Step 2: [Next step]
[...]
```

**Requirements:**

- Every formula written out explicitly, with each variable defined the first time it appears.
- Every calculation shown, with intermediate values.
- Units carried through and consistent throughout (SI unless field convention dictates otherwise).
- All assumptions made in the solution that were not stated in the question — flagged explicitly. (Ideally, they should already be in the question.)
- Precise technical language; no colloquialisms.
- No meta-commentary about AI, models, or "what the model got wrong." Keep the solution purely scientific.
- LaTeX for all non-text content.
- If you cite a source for a non-obvious fact, cite a peer-reviewed paper (a journal or peer-reviewed conference proceedings such as NeurIPS, ICML or STOC). Do not cite blogs, Wikipedia, textbooks, lecture notes, or preprints that have not been peer reviewed.

### 7. Grading rubric

Every question needs a rubric. It is used to grade AI responses to your question as correct, partially correct or incorrect, so it has to be objective: two experts applying it to the same response should always agree.

**Criteria (3 to 5, worth 10 points in total):**

- **Exactly one criterion is the final-answer criterion.** Tick it as the final answer. It must state the actual answer, e.g. "Gives 5/325/325/32, or an exactly equivalent value". Do not write "gives the correct answer". Give it the most points (usually 5).
- **The other criteria are key intermediate results or decisive steps** from your solution, each one checkable: a specific value, identity, classification or choice. e.g. "Identifies the point group as D3hD_{3h}D3h​", "Uses FA=1/4F_A = 1/4FA​=1/4 for the common ancestor".
- Each criterion is one yes/no check, and criteria do not overlap.

**Not acceptable as criteria:**

- Subjective quality: "explains clearly", "good reasoning", "well organised".
- Things almost any attempt does: "attempts the problem", "shows some working", "uses perturbation theory".
- A vague final answer: "arrives at the right value".

**How a response is labelled** (the same rule for every question):

- **Correct:** right final answer (the final-answer criterion is met).
- **Partially correct:** wrong final answer, but at least one other criterion is met.
- **Incorrect:** wrong final answer and no other criterion met.

**Common wrong answers (optional, recommended):** the plausible wrong answers a strong solver would reach, e.g. by missing the key step. Each must differ from the correct answer. These are the traps that make the question hard, and reviewers use them when grading.

### 8. Automated checks

There are no checks to run in the editor. After you submit, Summit's automated checks:

- check the question isn't a duplicate of an existing one;
- review it for quality problems (ambiguity, answer-key alignment, missing information, image use);
- check the rubric: the final-answer criterion must match your answer, no common wrong answer may equal it, and criteria must be objective;
- check whether the question or its answer can be found online;
- test the question on AI models against the difficulty target.

A question the checks flag comes back to you with written reasons. Fix what they name and submit again.

You do not need to run models in separate consumer chats, upload model screenshots, or record model answers manually.

## Complete worked examples

### Overview

> **About these examples:** They show format, completeness, and submission structure only — not the difficulty bar. Your live submissions should be harder than these samples (deeper synthesis, less lookupable, more image-load-bearing).

### Physics

**Subject domain:** Physics  
**Sub-topic:** Non-relativistic quantum mechanics / perturbation theory  
**Task type:** #1 — image-anchored quantitative derivation

**Image** (described here; real submission uploads the file): A one-dimensional infinite square well of width LLL on [0,L][0,L][0,L], drawn with vertical walls, and a single narrow spike at x=L/2x=L/2x=L/2 labeled V(x)=λ δ(x−L/2)V(x)=\lambda\,\delta(x-L/2)V(x)=λδ(x−L/2) with λ>0\lambda>0λ>0. The figure is required: the perturbation's location at the well centre is given only by the image.

**Question:** A particle of mass mmm is in the infinite square well shown on [0,L][0,L][0,L]. A perturbation V(x)=λ δ(x−L/2)V(x)=\lambda\,\delta(x-L/2)V(x)=λδ(x−L/2), with λ>0\lambda>0λ>0, is added at the position indicated in the figure. Working to first order in λ\lambdaλ, give the energy shift of the nnn-th eigenstate for general integer n≥1n\ge 1n≥1. Express the answer in terms of λ\lambdaλ, LLL and nnn.

**Final answer:** En(1)=2λLE_n^{(1)} = \dfrac{2\lambda}{L}En(1)​=L2λ​ for odd nnn, and En(1)=0E_n^{(1)} = 0En(1)​=0 for even nnn.

**Step-by-step solution:**

1. **Unperturbed eigenstates.** The normalised eigenfunctions of the infinite square well on [0,L][0,L][0,L] are ψn(x)=2/L⋅sin⁡(nπx/L)\psi_n(x) = \sqrt{2/L}\cdot\sin(n\pi x/L)ψn​(x)=2/L​⋅sin(nπx/L), n=1,2,3,…n = 1,2,3,\ldotsn=1,2,3,…
2. **First-order energy shift.** For a perturbation V(x)V(x)V(x), non-degenerate first-order perturbation theory gives En(1)=⟨ψn∣V∣ψn⟩=∫0L∣ψn(x)∣2V(x) dxE_n^{(1)} = \langle\psi_n|V|\psi_n\rangle = \int_0^L |\psi_n(x)|^2 V(x)\,dxEn(1)​=⟨ψn​∣V∣ψn​⟩=∫0L​∣ψn​(x)∣2V(x)dx.
3. **Evaluate the delta integral.** With V(x)=λ⋅δ(x−L/2)V(x) = \lambda\cdot\delta(x-L/2)V(x)=λ⋅δ(x−L/2), the integral collapses to the integrand at x=L/2x = L/2x=L/2: En(1)=λ⋅∣ψn(L/2)∣2E_n^{(1)} = \lambda\cdot|\psi_n(L/2)|^2En(1)​=λ⋅∣ψn​(L/2)∣2.
4. **Value at the centre.** ∣ψn(L/2)∣2=(2/L)⋅sin⁡2(nπ/2)|\psi_n(L/2)|^2 = (2/L)\cdot\sin^2(n\pi/2)∣ψn​(L/2)∣2=(2/L)⋅sin2(nπ/2). sin⁡(nπ/2)=±1\sin(n\pi/2) = \pm 1sin(nπ/2)=±1 for odd nnn and 000 for even nnn, so sin⁡2(nπ/2)=1\sin^2(n\pi/2) = 1sin2(nπ/2)=1 (odd nnn), 000 (even nnn).
5. **Assemble.** En(1)=λ⋅(2/L)⋅sin⁡2(nπ/2)=2λ/LE_n^{(1)} = \lambda\cdot(2/L)\cdot\sin^2(n\pi/2) = 2\lambda/LEn(1)​=λ⋅(2/L)⋅sin2(nπ/2)=2λ/L for odd nnn, and 000 for even nnn. Even states have a node at the well centre, so the centred delta does not shift them.

**Answer:** En(1)=2λ/LE_n^{(1)} = 2\lambda/LEn(1)​=2λ/L (odd nnn); 000 (even nnn).

**Rubric:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Criterion Points|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 (final answer) Gives En(1)=2λ/LE_n^{(1)} = 2\lambda/LEn(1)​=2λ/L for odd nnn and 000 for even nnn 5|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2 Uses the normalised eigenfunctions ψn(x)=2/Lsin⁡(nπx/L)\psi_n(x)=\sqrt{2/L}\sin(n\pi x/L)ψn​(x)=2/L​sin(nπx/L) 1|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 3 Reduces the first-order shift to λ ∣ψn(L/2)∣2\lambda\,\lvert\psi_n(L/2)\rvert^2λ∣ψn​(L/2)∣2 2|  |  |  | | --- | --- | --- | | 4 Shows sin⁡2(nπ/2)\sin^2(n\pi/2)sin2(nπ/2) is 111 for odd nnn and 000 for even nnn (even states have a node at L/2L/2L/2) 2 | | | | | | | | | | | | | | |

**Common wrong answers:** 2λ/L2\lambda/L2λ/L for all nnn (misses the node of the even states); λ/L\lambda/Lλ/L (normalises with 1/L1/\sqrt{L}1/L​ instead of 2/L\sqrt{2/L}2/L​).

### Chemistry

**Subject domain:** Chemistry  
**Sub-topic:** Molecular symmetry / vibrational spectroscopy (group theory)  
**Task type:** #2 — image-anchored classification/identification (discrete count)

**Image** (described here; real submission uploads the file): A three-dimensional structural drawing of a phosphorus pentafluoride (PF5\mathrm{PF}_5PF5​) molecule in its trigonal-bipyramidal geometry: one P atom at the centre, two axial P–F bonds drawn vertically, three equatorial P–F bonds at 120∘120^\circ120∘ in the horizontal plane, with axial and equatorial fluorines visibly distinguished. The figure is required: the specific geometry (which fixes the point group) is given only by the image, not stated in words.

**Question:** For the molecule shown, determine the number of fundamental vibrational modes that are active in both the infrared and the Raman spectra. Give a single integer.

**Final answer:** 333

**Step-by-step solution:**

1. **Assign the point group.** The trigonal-bipyramidal PF5\mathrm{PF}_5PF5​ shown belongs to D3hD_{3h}D3h​ (a C3C_3C3​ principal axis, three C2C_2C2​ axes, σh\sigma_hσh​, S3S_3S3​, σv\sigma_vσv​).
2. **Build the reducible representation of all 3N3N3N Cartesian displacements** (N=6N=6N=6, so 3N=183N=183N=18). Counting unmoved atoms per operation and multiplying by the per-atom contribution gives the characters of Γtot\Gamma_{\mathrm{tot}}Γtot​ over the D3hD_{3h}D3h​ classes.
3. **Reduce using the D3hD_{3h}D3h​ character table** to obtain Γtot\Gamma_{\mathrm{tot}}Γtot​ (dimension check: 181818).
4. **Remove translations and rotations.** Translations span A2′′+E′A_2''+E'A2′′​+E′; rotations span A2′+E′′A_2'+E''A2′​+E′′. Subtracting yields the vibrational representation Γvib\Gamma_{\mathrm{vib}}Γvib​ (dimension 121212).
5. **Apply the activity rules.** IR-active modes transform as A2′′A_2''A2′′​ or E′E'E′. Raman-active modes transform as the quadratics: A1′A_1'A1′​, E′E'E′, E′′E''E′′. The only symmetry species active in both is E′E'E′.
6. **Count the E′E'E′ modes in Γvib\Gamma_{\mathrm{vib}}Γvib​:** there are 333. Because D3hD_{3h}D3h​ has no centre of inversion, the rule of mutual exclusion does not apply, so these three E′E'E′ fundamentals appear in both spectra.

**Answer:** 333

**Rubric:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Criterion Points|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 (final answer) Gives 333 5|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2 Identifies the point group as D3hD_{3h}D3h​ 2|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 3 Identifies E′E'E′ as the only species that is both IR- and Raman-active, and finds 3 E′E'E′ modes in Γvib\Gamma_{\mathrm{vib}}Γvib​ 2|  |  |  | | --- | --- | --- | | 4 States that mutual exclusion does not apply because D3hD_{3h}D3h​ has no centre of inversion 1 | | | | | | | | | | | | | | |

**Common wrong answers:** 000 (applies the rule of mutual exclusion as if there were a centre of inversion).

### Biology

**Subject domain:** Biology  
**Sub-topic:** Population / quantitative genetics (pedigree inbreeding)  
**Task type:** #1 — image-anchored quantitative derivation

**Image** (described here; real submission uploads the file): A standard pedigree chart (squares = males, circles = females, horizontal lines = matings, vertical drop-lines = offspring). Reading top to bottom: an unrelated founder couple produces two full-sib offspring who mate with each other to produce individual A; A then mates with two different unrelated, non-inbred partners to produce B and C; and B and C mate to produce the target individual X. The figure is required: the mating loop that makes A inbred, and the half-sib relationship of B and C through A, are shown only in the pedigree.

**Question:** Using the pedigree shown, and assuming all founders are non-inbred and unrelated, compute the coefficient of inbreeding FXF_XFX​ of individual X. Give an exact fraction.

**Final answer:** 532\dfrac{5}{32}325​

**Step-by-step solution:**

1. **Identify the loop.** B and C share exactly one parent, A (their other parents are unrelated founders), so B and C are half-siblings and A is their only common ancestor.
2. **Wright's path formula.** FX=∑(1/2)n1+n2+1(1+FA)F_X = \sum (1/2)^{n_1+n_2+1}(1+F_A)FX​=∑(1/2)n1​+n2​+1(1+FA​), summed over common ancestors, where n1n_1n1​ and n2n_2n2​ are the numbers of generational links from each parent of X up to the common ancestor.
3. **Count links.** From B up to A is 111 link; from C up to A is 111 link. So the path term is (1/2)1+1+1(1+FA)=(1/8)(1+FA)(1/2)^{1+1+1}(1+F_A) = (1/8)(1+F_A)(1/2)1+1+1(1+FA​)=(1/8)(1+FA​).
4. **Correct for the ancestor's own inbreeding.** A is the offspring of a full-sib mating, so A is itself inbred with FA=1/4F_A = 1/4FA​=1/4. The (1+FA)(1+F_A)(1+FA​) factor is therefore 5/45/45/4.
5. **Assemble.** FX=(1/8)⋅(5/4)=5/32F_X = (1/8)\cdot(5/4) = 5/32FX​=(1/8)⋅(5/4)=5/32.

**Answer:** 5/325/325/32

**Rubric:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Criterion Points|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 (final answer) Gives 5/325/325/32, or an exactly equivalent value 5|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2 Identifies A as the only common ancestor of B and C, with path term (1/2)3(1/2)^3(1/2)3 2|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 3 Uses FA=1/4F_A = 1/4FA​=1/4 (A is the offspring of a full-sib mating) 2|  |  |  | | --- | --- | --- | | 4 Applies the (1+FA)(1+F_A)(1+FA​) correction to the path term 1 | | | | | | | | | | | | | | |

**Common wrong answers:** 1/81/81/8 (omits the (1+FA)(1+F_A)(1+FA​) correction).

### Mathematics

**Subject domain:** Mathematics  
**Sub-topic:** Algebraic geometry (plane curve singularities, geometric genus)  
**Task type:** #1 — image-anchored quantitative derivation

**Image** (described here; real submission uploads the file): The real locus of an irreducible complex projective plane curve CCC of degree 666, drawn with its five singular points marked. Each singular point is labelled with its local analytic normal form: P1P_1P1​ and P2P_2P2​ are nodes (x2−y2=0x^2-y^2=0x2−y2=0), P3P_3P3​ is a cusp (y2−x3=0y^2-x^3=0y2−x3=0), P4P_4P4​ is a tacnode (y2−x4=0y^2-x^4=0y2−x4=0), and P5P_5P5​ is an ordinary triple point (three smooth branches meeting pairwise transversally). The figure is required: the number, and above all the analytic type, of each singularity is given only by the diagram, and the genus cannot be computed without it.

**Question:** Let CCC be the degree-666 irreducible plane curve shown, whose only singularities are the five marked points with the indicated local types. Compute the geometric genus ggg of CCC (the genus of its normalisation). Give a single non-negative integer.

**Final answer:** g=2g = 2g=2

**Step-by-step solution:**

1. **Arithmetic genus.** For a plane curve of degree ddd, the arithmetic genus is pa=(d−12)p_a = \binom{d-1}{2}pa​=(2d−1​). With d=6d=6d=6, pa=(52)=10p_a = \binom{5}{2} = 10pa​=(25​)=10.
2. **Genus drop from singularities.** The geometric genus is g=pa−∑pδpg = p_a - \sum_{p} \delta_pg=pa​−∑p​δp​, where δp\delta_pδp​ is the delta-invariant of the singularity at ppp. For a plane curve singularity with Milnor number μ\muμ and rrr local branches, δ=μ+r−12\delta = \tfrac{\mu + r - 1}{2}δ=2μ+r−1​.
3. **Delta-invariants of the five points.** Node A1A_1A1​ (μ=1\mu=1μ=1, r=2r=2r=2): δ=1+2−12=1\delta = \tfrac{1+2-1}{2} = 1δ=21+2−1​=1; there are two, contributing 222. Cusp A2A_2A2​ (μ=2\mu=2μ=2, r=1r=1r=1): δ=2+1−12=1\delta = \tfrac{2+1-1}{2} = 1δ=22+1−1​=1. Tacnode A3A_3A3​ (μ=3\mu=3μ=3, r=2r=2r=2): δ=3+2−12=2\delta = \tfrac{3+2-1}{2} = 2δ=23+2−1​=2. Ordinary triple point D4D_4D4​ (μ=4\mu=4μ=4, r=3r=3r=3): δ=4+3−12=3\delta = \tfrac{4+3-1}{2} = 3δ=24+3−1​=3 (equivalently (32)=3\binom{3}{2}=3(23​)=3 for an ordinary triple point).
4. **Total delta.** ∑pδp=1+1+1+2+3=8\sum_p \delta_p = 1 + 1 + 1 + 2 + 3 = 8∑p​δp​=1+1+1+2+3=8.
5. **Assemble.** g=pa−∑pδp=10−8=2g = p_a - \sum_p \delta_p = 10 - 8 = 2g=pa​−∑p​δp​=10−8=2.

**Answer:** g=2g = 2g=2

**Rubric:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Criterion Points|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 (final answer) Gives g=2g = 2g=2 5|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2 Uses arithmetic genus pa=10p_a = 10pa​=10 for degree 6 1|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 3 Uses δ=2\delta = 2δ=2 for the tacnode and δ=3\delta = 3δ=3 for the ordinary triple point 3|  |  |  | | --- | --- | --- | | 4 Finds total ∑pδp=8\sum_p \delta_p = 8∑p​δp​=8 1 | | | | | | | | | | | | | | |

**Common wrong answers:** 555 (treats all five points as nodes); 444 (gives the tacnode δ=2\delta = 2δ=2 but the triple point δ=1\delta = 1δ=1).

### Computer Science/AI

**Subject domain:** Computer Science/AI  
**Sub-topic:** Analysis of algorithms (recurrences)  
**Task type:** text-only (`not_applicable`)

**Image:** none. The procedure is given as code in the question, so the stem stands alone.

**Question:** Consider the procedure below, where `work()` takes constant time. Assume nnn is a power of 2. Give a tight bound on the running time T(n)T(n)T(n) of `P(n)` in Θ\ThetaΘ notation, in simplest form.

```
procedure P(n):
    if n <= 1: return
    for i = 1 to n:
        for j = i to n step i:
            work()
    P(n/2)
    P(n/2)
```

**Final answer:** Θ(nlog⁡2n)\Theta(n \log^2 n)Θ(nlog2n)

**Step-by-step solution:**

1. **Inner loop count.** For a fixed iii, `j` runs over i,2i,3i,…≤ni, 2i, 3i, \ldots \le ni,2i,3i,…≤n, which is ⌊n/i⌋\lfloor n/i \rfloor⌊n/i⌋ iterations.
2. **Total non-recursive work.** ∑i=1n⌊n/i⌋=nHn−O(n)=Θ(nlog⁡n)\sum_{i=1}^{n} \lfloor n/i \rfloor = n H_n - O(n) = \Theta(n \log n)∑i=1n​⌊n/i⌋=nHn​−O(n)=Θ(nlogn), where Hn=∑i=1n1/i=ln⁡n+O(1)H_n = \sum_{i=1}^{n} 1/i = \ln n + O(1)Hn​=∑i=1n​1/i=lnn+O(1) is the nnn-th harmonic number.
3. **Recurrence.** Two recursive calls on size n/2n/2n/2 plus the loops give T(n)=2T(n/2)+Θ(nlog⁡n)T(n) = 2T(n/2) + \Theta(n \log n)T(n)=2T(n/2)+Θ(nlogn).
4. **Solve by recursion tree.** At depth kkk there are 2k2^k2k calls of size n/2kn/2^kn/2k, each costing Θ((n/2k)log⁡(n/2k))\Theta\big((n/2^k)\log(n/2^k)\big)Θ((n/2k)log(n/2k)), so depth kkk costs Θ(n(log⁡2n−k))\Theta\big(n(\log_2 n - k)\big)Θ(n(log2​n−k)). Summing over k=0,…,log⁡2n−1k = 0, \ldots, \log_2 n - 1k=0,…,log2​n−1 gives Θ(n⋅log⁡2n(log⁡2n+1)2)=Θ(nlog⁡2n)\Theta\big(n \cdot \tfrac{\log_2 n(\log_2 n + 1)}{2}\big) = \Theta(n \log^2 n)Θ(n⋅2log2​n(log2​n+1)​)=Θ(nlog2n). (Equivalently, the extended master theorem with f(n)=Θ(nlog⁡22log⁡1n)f(n) = \Theta(n^{\log_2 2}\log^1 n)f(n)=Θ(nlog2​2log1n).)

**Answer:** Θ(nlog⁡2n)\Theta(n \log^2 n)Θ(nlog2n)

**Rubric:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Criterion Points|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 (final answer) Gives Θ(nlog⁡2n)\Theta(n \log^2 n)Θ(nlog2n) 5|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2 Finds the nested loops do Θ(nlog⁡n)\Theta(n \log n)Θ(nlogn) work (harmonic sum ∑i⌊n/i⌋\sum_i \lfloor n/i \rfloor∑i​⌊n/i⌋) 2|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 3 Sets up T(n)=2T(n/2)+Θ(nlog⁡n)T(n) = 2T(n/2) + \Theta(n \log n)T(n)=2T(n/2)+Θ(nlogn) 2|  |  |  | | --- | --- | --- | | 4 Solves it by a recursion tree with per-level cost Θ(n(log⁡n−k))\Theta(n(\log n - k))Θ(n(logn−k)), or by the extended master theorem 1 | | | | | | | | | | | | | | |

**Common wrong answers:** Θ(n2)\Theta(n^2)Θ(n2) (treats the nested loops as quadratic); Θ(nlog⁡n)\Theta(n \log n)Θ(nlogn) (treats the nested loops as linear).

### Engineering

**Subject domain:** Engineering  
**Sub-topic:** Control systems (closed-loop stability)  
**Task type:** #1 — image-anchored quantitative derivation

**Image** (described here; real submission uploads the file): A negative-feedback block diagram. The reference R(s)R(s)R(s) enters a summing junction (+ on the reference, − on the feedback), then a gain block KKK, then the plant G(s)=1s(s+1)(s+2)G(s) = \dfrac{1}{s(s+1)(s+2)}G(s)=s(s+1)(s+2)1​, giving the output Y(s)Y(s)Y(s). The output is fed back through a sensor block H(s)=3s+3H(s) = \dfrac{3}{s+3}H(s)=s+33​ to the − input of the junction. Time is in seconds. The figure is required: the sensor dynamics in the feedback path are given only by the diagram.

**Question:** For the closed-loop system shown, find the controller gain K>0K > 0K>0 at which the system becomes marginally stable. Give an exact value.

**Final answer:** K=10/3K = 10/3K=10/3

**Step-by-step solution:**

1. **Loop transfer function.** With the sensor in the feedback path, L(s)=K G(s) H(s)=3Ks(s+1)(s+2)(s+3)L(s) = K\,G(s)\,H(s) = \dfrac{3K}{s(s+1)(s+2)(s+3)}L(s)=KG(s)H(s)=s(s+1)(s+2)(s+3)3K​.
2. **Characteristic equation.** 1+L(s)=01 + L(s) = 01+L(s)=0 gives s(s+1)(s+2)(s+3)+3K=0s(s+1)(s+2)(s+3) + 3K = 0s(s+1)(s+2)(s+3)+3K=0. Expanding, s4+6s3+11s2+6s+3K=0s^4 + 6s^3 + 11s^2 + 6s + 3K = 0s4+6s3+11s2+6s+3K=0.
3. **Routh array.**
   - s4s^4s4: 1, 11, 3K1,\ 11,\ 3K1, 11, 3K
   - s3s^3s3: 6, 66,\ 66, 6
   - s2s^2s2: 6⋅11−1⋅66=10, 3K\tfrac{6 \cdot 11 - 1 \cdot 6}{6} = 10,\ 3K66⋅11−1⋅6​=10, 3K
   - s1s^1s1: 10⋅6−6⋅3K10=6−1.8K\tfrac{10 \cdot 6 - 6 \cdot 3K}{10} = 6 - 1.8K1010⋅6−6⋅3K​=6−1.8K
   - s0s^0s0: 3K3K3K
4. **Stability condition.** All first-column entries are positive when 3K>03K > 03K>0 and 6−1.8K>06 - 1.8K > 06−1.8K>0, i.e. 0<K<10/30 < K < 10/30<K<10/3. The system is marginally stable at K=10/3K = 10/3K=10/3, where the s1s^1s1 row is zero.
5. **Check the oscillation.** At K=10/3K = 10/3K=10/3 the auxiliary equation from the s2s^2s2 row is 10s2+10=010s^2 + 10 = 010s2+10=0, so s=±js = \pm js=±j: a sustained oscillation at ω=1\omega = 1ω=1 rad/s. Substituting s=js = js=j into the characteristic equation gives 1−6j−11+6j+3K=01 - 6j - 11 + 6j + 3K = 01−6j−11+6j+3K=0, i.e. 3K=103K = 103K=10, confirming K=10/3K = 10/3K=10/3.

**Answer:** K=10/3K = 10/3K=10/3

**Rubric:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Criterion Points|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 (final answer) Gives K=10/3K = 10/3K=10/3, or an exactly equivalent value 5|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2 Includes the sensor in the loop: characteristic equation s4+6s3+11s2+6s+3K=0s^4 + 6s^3 + 11s^2 + 6s + 3K = 0s4+6s3+11s2+6s+3K=0 2|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 3 Finds the Routh s1s^1s1 entry 6−1.8K6 - 1.8K6−1.8K (or an equivalent condition from the array) 2|  |  |  | | --- | --- | --- | | 4 Identifies the crossing at s=±js = \pm js=±j (ω=1\omega = 1ω=1 rad/s) 1 | | | | | | | | | | | | | | |

**Common wrong answers:** 666 (ignores the sensor and uses s(s+1)(s+2)+K=0s(s+1)(s+2) + K = 0s(s+1)(s+2)+K=0); 101010 (uses the sensor's pole but drops its gain of 3).

### Difficulty flavour by task type

What a submittable hard question feels like:

- **#1 derivation:** a setup needing synthesis across two subfields, or a non-obvious framework choice — e.g. equilibrium conformer population from molecular-mechanics strain energies plus a Boltzmann factor, where models default to DFT ΔG values.
- **#2 classification:** an object where the answer turns on ruling out a near-neighbour category — e.g. the named vicariance event that fits an inferred divergence date from a calibrated molecular clock, not a one-glance label.
- **#3 reasoning:** a process with several plausible answers where the right one depends on research-grade evidence — e.g. the step with the most carbanion character in a catalytic cycle, triangulated from a Hammett ρ and a kinetic isotope effect given in the figure.
- **#4 graph extraction:** a plot where the reading is non-trivial and feeds a graduate computation — e.g. extract a rate from a non-linear Arrhenius plot you generated, then compute an activation entropy.



## Review process

1. You submit through Summit. The automated checks run first and may return the question to you with written reasons.
2. **First reviewer (grader).** An expert in your domain checks your solution step by step, grades each AI attempt against your rubric, and may improve the rubric (e.g. to credit a valid approach it missed). They may also add equivalent forms of your answer to Also accepted.
3. **Second reviewer (final grader).** A different expert in your domain grades the AI attempts independently, checks the first reviewer's rubric changes, and makes the final decision: accept, or send back to you.
4. Reviewers only change the rubric and the accepted answer forms. Anything in the question, answer or solution that needs fixing comes back to you with the reviewer's reasons. Fix those issues and submit again from My submissions; the question goes through the automated checks and review again.
5. A question can only be sent back by reviewers a limited number of times. After that, it is rejected for good.
6. Once a reviewer claims a question, your submitted version is read-only.

## Questions returned to add a rubric

Questions submitted before rubrics existed, including accepted ones, may be returned to you with a banner asking you to add a rubric. Add the rubric (and fix anything else the return names) and submit again. The question then goes through the full automated checks, including the difficulty test, and review again.

## Final checklist before submitting

- Question is at graduate/PhD level (not undergraduate)
- Difficulty comes from the reasoning, not from long calculation, and the answer can't be found by running a short program or brute force
- Single question, single answer, not compound
- All assumptions stated in the question, including the required precision for numeric answers
- Answer doesn't depend on software versions, hardware, recent model behaviour, or a design code you didn't quote
- Non-searchable (you Googled it yourself and confirmed)
- Original work, not copied or lightly paraphrased
- LaTeX used for all non-text content; code in code blocks
- Image is self-made using permitted tools (not AI-generated, not from the web), or text-only within the soft no-image allowance
- Image is clean, labeled, and necessary to answer the question (when used)
- Final answer is bare (no fluff); equivalent forms listed in Also accepted
- Solution has numbered steps with every formula and calculation written out
- Units are SI and consistent throughout
- Rubric: 3–5 objective criteria, 10 points total, one final-answer criterion that states the actual answer
- Common wrong answers listed, each different from the correct answer
- No meta-commentary about AI in the solution

Submit. Track the final status from Previously submitted.

Questions about the process go to the project lead. Questions about your subject matter — you're the expert.
