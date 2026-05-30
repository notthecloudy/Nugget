import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: root
    color: "transparent"

    Column {
        anchors.fill: parent
        anchors.margins: 24
        spacing: 12

        Text {
            text: "Settings"
            color: "white"
            font.pixelSize: 24
            font.bold: true
        }

        Text {
            text: "Migration preview: QWidget fallback remains active."
            color: "#C4CAD3"
            font.pixelSize: 13
        }

        Rectangle {
            width: parent.width
            height: 54
            radius: 8
            color: "#2F3640"

            Text {
                anchors.centerIn: parent
                text: "Selected Device: " + shellBridge.progress
                color: "#EAF1FF"
                font.pixelSize: 12
            }
        }
    }
}
