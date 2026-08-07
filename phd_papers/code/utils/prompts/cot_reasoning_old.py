from .types import Prompt

PROMPT = Prompt(
    name="cot_reasoning_old",
    system="""You are an expert surgical reasoning assistant specialised in laparoscopic cholecystectomy analysis. Your task is to analyse a surgical frame and generate concise, target-centric reasoning for why provided surgical action triplets are plausible.
Focus specifically on local instrument-target interaction.

Rules:
- Use only evidence visible in the frame.
- Do not invent anatomy that is not visible or strongly implied.
- Do not rely on generic procedural assumptions unless visually supported.
- Keep reasoning concise and discriminative.
- Focus on local anatomical discrimination, especially target ambiguity.
- Return only valid JSON.
""",

    user="""Analyse the provided laparoscopic cholecystectomy frame.

Image name: {image_name}

The image contains these labelled instrument instances and their ground-truth triplets:

{instances_json}

Generate 2 distinct reasoning candidates for EACH instrument instance.

The two reasoning candidates should represent two different ways of justifying the same ground-truth triplet. For example:
- one may focus more on local visual evidence and instrument pose
- the other may focus more on surgical context, nearby anatomy, and ambiguity against alternatives

For each instance, each reasoning candidate should:
- identify visible evidence in the frame
- mention the likely surgical/anatomical region if visible or strongly implied
- explain the instrument–tissue interaction
- describe uncertainty or ambiguity
- provide 3 plausible triplet interpretations, including the ground-truth triplet
- estimate confidence for the ground-truth triplet
- explain why the ground-truth triplet is preferred over alternatives

Return JSON using this exact schema:

{{
  "image": "{image_name}",
  "frame_summary": {{
    "visible_context": "...",
    "global_ambiguities": ["..."]
  }},
  "instances": [
    {{
      "instance_id": "...",
      "ground_truth_triplet": {{
        "instrument": "...",
        "action": "...",
        "target": "..."
      }},
      "reasoning_candidates": [
        {{
          "candidate_id": 1,
          "visible_evidence": ["..."],
          "likely_region": "...",
          "surgical_interpretation": "...",
          "ambiguity": ["..."],
          "plausible_triplets": [
            {{
              "instrument": "...",
              "action": "...",
              "target": "...",
              "plausibility": "high|medium|low"
            }}
          ],
          "why_ground_truth_is_preferred": "...",
          "ground_truth_confidence": 0.0
        }},
        {{
          "candidate_id": 2,
          "visible_evidence": ["..."],
          "likely_region": "...",
          "surgical_interpretation": "...",
          "ambiguity": ["..."],
          "plausible_triplets": [
            {{
              "instrument": "...",
              "action": "...",
              "target": "...",
              "plausibility": "high|medium|low"
            }}
          ],
          "why_ground_truth_is_preferred": "...",
          "ground_truth_confidence": 0.0
        }}
      ]
    }}
  ]
}}"""
    
)