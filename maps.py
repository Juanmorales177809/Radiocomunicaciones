import sys
from web import *
from PyQt5.QtGui import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebView

html= \
"""
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

function initMap() {
  var myLatLng = {lat: -25.363 , lng: 131.044 };

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Mapa Prueba!'
  });
}

    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=API_KEY&signed_in=true&callback=initMap"></script>
  </body>
</html>
"""     

class FormularioLogin(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        QWebView.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
   
        
if __name__== "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = FormularioLogin()
    myapp.ui.webView.setHtml(html)
    myapp.show()
    sys.exit(app.exec_())
                                 