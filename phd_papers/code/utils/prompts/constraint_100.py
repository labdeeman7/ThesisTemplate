from .types import Prompt

PROMPT = Prompt(
    name="constraint_100",
    system="""Return ONLY valid JSON. Output an object with a single key "predictions", containing a list of items. Each item must have keys: id, instrument, action, target. Use only the allowed labels.
If idle: action="no action", target="no target". No text outside JSON. 
Allowed labels:
Instruments = ['Grasping Forceps','Bipolar Forceps','Monopolar Hook','Laparoscopic Scissors','Clip Applier','Suction-Irrigator']
Actions = ['grasp','retract','dissect','coagulate','clip','cut','aspirate','irrigate','pack','no action']
Targets = ['gallbladder','cystic plate','cystic duct','cystic artery','cystic pedicle','blood vessel','fluid',
           'abdominal wall cavity','liver','adhesion','omentum','peritoneum',
           'gastrointestinal tract','specimen bag','no target']         
           
Valid Combinations (Instrument: {Action: [Targets]}):
- Grasping Forceps: {dissect: [cystic plate, gallbladder, omentum], grasp: [cystic artery, cystic duct, cystic pedicle, cystic plate, gallbladder, gastrointestinal tract, liver, omentum, peritoneum, specimen bag], pack: [gallbladder], retract: [cystic duct, cystic pedicle, cystic plate, gallbladder, gastrointestinal tract, liver, omentum, peritoneum], no action: [no target]}
- Bipolar Forceps: {coagulate: [abdominal wall cavity, blood vessel, cystic artery, cystic duct, cystic pedicle, cystic plate, gallbladder, liver, omentum, peritoneum], dissect: [adhesion, cystic artery, cystic duct, cystic plate, gallbladder, omentum], grasp: [cystic plate, liver, specimen bag], retract: [cystic duct, cystic pedicle, gallbladder, liver, omentum], no action: [no target]}
- Monopolar Hook: {coagulate: [blood vessel, cystic artery, cystic duct, cystic pedicle, cystic plate, gallbladder, liver, omentum], cut: [blood vessel, peritoneum], dissect: [blood vessel, cystic artery, cystic duct, cystic plate, gallbladder, omentum, peritoneum], retract: [gallbladder, liver], no action: [no target]}
- Laparoscopic Scissors: {coagulate: [omentum], cut: [adhesion, blood vessel, cystic artery, cystic duct, cystic plate, liver, omentum, peritoneum], dissect: [cystic plate, gallbladder, omentum], no action: [no target]}
- Clip Applier: {clip: [blood vessel, cystic artery, cystic duct, cystic pedicle, cystic plate], no action: [no target]}
- Suction-Irrigator: {aspirate: [fluid], dissect: [cystic duct, cystic pedicle, cystic plate, gallbladder, omentum], irrigate: [abdominal wall cavity, cystic pedicle, liver], retract: [gallbladder, liver, omentum], no action: [no target]}

Each predicted (instrument, action, target) MUST exactly match one of the allowed triplets listed above. Do NOT output any combination outside this list.
""",
    user="""You are analysing a laparoscopic cholecystectomy frame.
The image contains multiple surgical instrument instances predicted by a neural network.
Each instance is marked in the image with a name and ID (e.g. grasper_1, hook_2).
For EACH instance ID, assign exactly one (instrument, action, target) triplet using visual evidence.
  
Required output format (example):
{{
  "predictions": [
    {{"id": "grasper_1", "instrument": "Grasping Forceps", "action": "retract", "target": "gallbladder"}},
    {{"id": "hook_2", "instrument": "Monopolar Hook", "action": "dissect", "target": "cystic plate"}}
  ]
}}
Instrument Instances to label (from the overlay): {instrument_list}
Now produce the JSON for this image."""
)
