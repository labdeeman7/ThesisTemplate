from .types import Prompt


PROMPT = Prompt(
    name="video_baseline",
    system="""Return ONLY valid JSON. Output an object with a single key "predictions", containing a list of items. Each item must have keys: id, instrument, action, target. Use only the allowed labels.
If idle: action="no action", target="no target". No text outside JSON.""",
    user="""You are analysing multiple temporally ordered laparoscopic cholecystectomy frames.
The centre/current frame is the only frame to label. Previous and next frames are context only; use them to understand motion, action, and target relationships, but do not output labels for instruments that appear only in neighbouring frames.
Instrument instance IDs come from the centre-frame overlay only.

Temporal image order:
{temporal_order}

Temporal spacing:
{temporal_spacing}
Use sample_fps={sample_fps} as the approximate temporal sampling rate for these selected frames.

Allowed labels:
Instruments = ['Grasping Forceps','Bipolar Forceps','Monopolar Hook','Laparoscopic Scissors','Clip Applier','Suction-Irrigator']
Actions = ['grasp','retract','dissect','coagulate','clip','cut','aspirate','irrigate','pack','no action']
Targets = ['gallbladder','cystic plate','cystic duct','cystic artery','cystic pedicle','blood vessel','fluid',
           'abdominal wall cavity','liver','adhesion','omentum','peritoneum',
           'gastrointestinal tract','specimen bag','no target']

Required output format (example):
{{
  "predictions": [
    {{"id": "grasper_1", "instrument": "Grasping Forceps", "action": "retract", "target": "gallbladder"}},
    {{"id": "hook_2", "instrument": "Monopolar Hook", "action": "dissect", "target": "cystic plate"}}
  ]
}}

Instrument instances to label from the centre-frame overlay: {instrument_list}
Now produce the JSON for the centre/current frame only.""",
)
