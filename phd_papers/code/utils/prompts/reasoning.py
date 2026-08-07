from .types import Prompt

PROMPT = Prompt(
    name="reasoning",
    system="""Return ONLY valid JSON. Output an object with a single key "reasoning_predictions", containing a list of items. Each item must have keys: id, reasoning, final_triplet. Use only the allowed labels for final_triplet.
If idle: action="no action", target="no target". No text outside JSON.""",
    user = """You are analysing a laparoscopic cholecystectomy frame.
The image contains multiple surgical instrument instances predicted by a neural network.
Each instance is marked in the image with a name and ID.
For EACH instance ID, first provide concise visual reasoning, then predict the final triplet.
Allowed labels:
Instruments = ['Grasping Forceps','Bipolar Forceps','Monopolar Hook','Laparoscopic Scissors','Clip Applier','Suction-Irrigator']
Actions = ['grasp','retract','dissect','coagulate','clip','cut','aspirate','irrigate','pack','no action']
Targets = ['gallbladder','cystic plate','cystic duct','cystic artery','cystic pedicle','blood vessel','fluid',
           'abdominal wall cavity','liver','adhesion','omentum','peritoneum',
           'gastrointestinal tract','specimen bag','no target']
Instrument Instances to label: {instrument_list}

Return JSON in this format:
{{
  "reasoning_predictions": [
    {{
      "id": "grasper_1",
      "reasoning": {{
        "visible_evidence": ["..."],
        "likely_region": "...",
        "surgical_interpretation": "...",
        "ambiguity": ["..."],
        "alternative_interpretations": [
          {{"instrument": "...", "action": "...", "target": "...", "plausibility": "medium"}}
        ],
        "weakness": "...",
        "why_final_triplet_is_preferred": "...",
        "confidence": 0.0
      }},
      "final_triplet": {{
        "instrument": "Grasping Forceps",
        "action": "retract",
        "target": "gallbladder"
      }}
    }}
  ]
}}

Now produce the JSON for this image."""

)
