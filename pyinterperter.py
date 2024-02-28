# d = []

# i=1
# while i <= 100:
#     d.append(i)
#     i+=1


# while len(d) !=0:
#     if len(d)>10:
#         d_list, d = d[:10], d[10:]
#     else:
#         d_list, d = d, []
        
#     print(d_list)
import html2text
import json

def fix_desc(desc: str):
    try:
        ret_desc = desc + '"'
        json.loads(ret_desc)
        print(f"Success -------------------------- \n\n {ret_desc}")
        return ret_desc
    except json.JSONDecodeError:
        if len(desc) > 0:
            print(f"Fixing again -------------------------- {len(desc)}")
            return fix_desc(desc[:-1])
        else:
            print("Cannot fix the description, returning the original.")
            return False

text_maker = html2text.HTML2Text()
text_maker.single_line_break = True
text_maker.unicode_snob = True
text_maker.body_width = 255
text_maker.ignore_images = True

desc = """
<p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Roll it to wherever you need it. It's also suitable to sit on and easily transforms into an extra chair for your guests. Durable and steady with a quality that will last for many years.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Product description</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">10 year guarantee. Read about the terms in the guarantee brochure.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Integrated damper closes the drawer silently and gently.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">You can customise and personalise your storage by putting magnets on the outside.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">You can manage your cables easily thanks to the convenient hole at the bottom.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Castors make it easy to roll the storage unit under your desk, or around the room.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Please refer to packaging label for country of origin.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">This storage unit has been tested for office use and meets the requirements for durability and stability set forth in the following standards: EN 14073, EN14074, ANSI/BIFMA x5.9 and ISO-7170.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">You can add ROTHULT smart lock for secure storage.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Product size</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Width: 41 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Depth: 45 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Height: 61 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Care instructions</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Storage unit on castors</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Wipe clean with a cloth dampened in a mild cleaner.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Storage unit/castor</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Wipe dry with a clean cloth.</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Environment &amp;amp; materials</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Materials</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Storage unit</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Top panel/ Shelf/ Bottom panel:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Particleboard, Melamine foil, Plastic edging</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Side panel/ Back panel/ Pen holder:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Steel, Epoxy/polyester powder coating</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Poles:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Aluminium, Epoxy/polyester powder coating</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Drawer front/ Drawer side/ Drawer back:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Particleboard, Oak veneer, Solid oak, Tinted clear acrylic lacquer</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Drawer bottom:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Particleboard, Oak veneer, Tinted clear acrylic lacquer, Paper foil</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Castor</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Pin:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Steel, Galvanized</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Nut:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Steel</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Bracket:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Steel, Powder coating</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Wheel/ Cover/ Brake:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Polyamide plastic</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Rubber part:</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Synthetic rubber</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">&nbsp;</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Package details&nbsp;</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Packages: 2&nbsp;</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">BEKANT</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">castor</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">003.724.58</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Width: 11 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Height: 3 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Length: 33 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Weight: 1.01 kg</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Package(s): 1</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">BEKANT</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">storage unit</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">603.629.89</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Width: 49 Cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Height: 13 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Length: 76 cm</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Weight: 19.34 kg</p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;"><br></p><p class="MsoNormal" style="margin-bottom: 0.0001pt; line-height: normal;">Package(s): 1</p>
"""
Desc = """{}""".format( text_maker.handle(desc))

json_desc = json.dumps(Desc, ensure_ascii=False)[:1800]

print(json_desc)

json_desc = fix_desc(json_desc)

print(json.loads(json_desc))