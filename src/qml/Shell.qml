import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: root
    width: 280
    height: 64
    color: "transparent"

    Rectangle {
        anchors.fill: parent
        radius: 10
        color: "#222831"
        opacity: shellBridge.busy ? 0.95 : 0.7

        Behavior on opacity {
            NumberAnimation { duration: 180 }
        }

        Text {
            anchors.centerIn: parent
            text: shellBridge.busy ? "Applying: " + shellBridge.progress : "Ready"
            color: "white"
            font.pixelSize: 13
            elide: Text.ElideRight
            width: parent.width - 20
            horizontalAlignment: Text.AlignHCenter
        }
    }
}
