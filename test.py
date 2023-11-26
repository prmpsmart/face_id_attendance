# from src.shared.commons import *

# a = QApplication([])

# img = QPixmap(r'C:\Users\USER\Desktop\Workspace\Jerry\assets\sample.svg')
# qp = QPainter(img)
# qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
# qp.fillRect( img.rect(), QColor('#05C847') )
# qp.end()
# print(img.save('check_n.png'))


import os

for r, t, d in os.walk('.'):
    for f in d:
        p = os.path.join(r, f)
        
        if os.path.splitext(p)[1] == '.pyc':
            print(f)
            # os.remove(p)
