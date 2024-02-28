import html2text

html = """<table border="0" cellpadding="0" cellspacing="0" width="498" style="width: 373pt;"><tbody><tr height="33" style="mso-height-source:userset;height:24.9pt">
  <td height="33" class="xl65" width="498" style="height:24.9pt;width:373pt">Plastic
  is a key material for IKEA and remains so going forward. It is strong,
  durable, lightweight and versatile. It is a main component in a large amount
  of our products and has a wide variety of applications from surface materials
  such as paint and foil, to screws and shelf pegs. There is a lot of valid
  concern regarding how plastic impacts the environment and at IKEA we take
  this very seriously. As part of our larger circular journey and transition
  from virgin fossil based material, we are working hard to change all plastic
  in our home furnishing products to plastic made from recycled and/or
  renewable raw materials.<br>
    See more<br>
    By combining different seating sections, you can create a sofa in a shape
  and size that perfectly suits your outdoor space.<br>
    Practical storage space under the seat.<br>
    The cushion color stays fresh longer as the cover is fade resistant.<br>
    You can just shake off water from a light rain, as the cushion cover is
  water repellent.<br>
    The cushion cover is easy to keep clean since it can be removed and machine
  washed.<br>
    You can have a personal touch to your sofa by adding one or more decorative
  cushions to your style and taste.<br>
    Please refer to packaging label for country of origin<br>
    Fittings to connect sections with included.<br>
    May be completed with TOSTERÃ– storage bag.<br>
    designer<br>
    Eva Lilja Löwenhielm <br>
    <br>
    &nbsp;Product dimensions<br>
    Width: 223 cm<br>
    Depth: 144 cm<br>
    Height: 88 cm<br>
    Seat width: 187 cm<br>
    Seat depth: 48 cm<br>
    Seat height: 44 cm<br>
    <br>
    &nbsp;Packaging info<br>
    This product comes as 19 packages<br>
    FRÃ–SÃ–N<br>
    cover for seat cushion<br>
    403.917.23<br>
    This product has multiple packages<br>
    Height :&nbsp; 4 cm<br>
    Length :&nbsp; 22 cm<br>
    Weight :&nbsp; 0.50 kg<br>
    Width: 17 cm<br>
    Number of packages : 4<br>
    <br>
    FRÃ–SÃ–N<br>
    cover for back cushion<br>
    103.917.29<br>
    This product has multiple packages<br>
    Height :&nbsp; 3 cm<br>
    Length :&nbsp; 22 cm<br>
    Weight :&nbsp; 0.35 kg<br>
    Width: 17 cm<br>
    Number of packages : 3<br>
    <br>
    SOLLERÃ–N<br>
    stool, outdoor<br>
    504.246.00<br>
    This product has multiple packages<br>
    Height :&nbsp; 11 cm<br>
    Length :&nbsp; 65 cm<br>
    Weight :&nbsp; 9.00 kg<br>
    Width: 65 cm<br>
    Number of packages : 1<br>
    <br>
    SOLLERÃ–N<br>
    one-seat section, outdoor<br>
    304.245.97<br>
    This product has multiple packages<br>
    Height :&nbsp; 24 cm<br>
    Length :&nbsp; 74 cm<br>
    Weight :&nbsp; 14.90 kg<br>
    Width: 65 cm<br>
    Number of packages : 3<br>
    <br>
    SOLLERÃ–N<br>
    armrest section, outdoor<br>
    204.245.88<br>
    This product has multiple packages<br>
    Height :&nbsp; 35 cm<br>
    Length :&nbsp; 84 cm<br>
    Weight :&nbsp; 11.15 kg<br>
    Width: 55 cm<br>
    Number of packages : 1<br>
    <br>
    DUVHOLMEN<br>
    inner cushion for back cushion<br>
    903.918.34<br>
    This product has multiple packages<br>
    Height :&nbsp; 14 cm<br>
    Length :&nbsp; 62 cm<br>
    Weight :&nbsp; 1.15 kg<br>
    Width: 44 cm<br>
    Number of packages : 3<br>
    <br>
    DUVHOLMEN<br>
    inner cushion for seat cushion<br>
    303.918.51<br>
    This product has multiple packages<br>
    Height :&nbsp; 8 cm<br>
    Length :&nbsp; 62 cm<br>
    Weight :&nbsp; 1.33 kg<br>
    Width: 62 cm<br>
    Number of packages : 4</td></tr></tbody></table>"""
text = "{}".format(html2text.html2text(html)[:2000])
print(text)

print(len(text))

