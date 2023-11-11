import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
	visible: true
	width: 800
	height: 600
	title: "GPT Assistant"

	function sendMessage() {
		var messageText = messageInput.text.trim();
		if (messageText !== "") {
			chatArea.append("You: " + messageText);
			chatClient.sendMessage(messageText);
			messageInput.text = "";
		}
	}

	RowLayout {
		anchors.fill: parent

		// Sidebar
		ListView {
			Layout.preferredWidth: 200
			model: ListModel {
				ListElement { title: "Home" }
				ListElement { title: "Settings" }
				ListElement { title: "About" }
			}
			delegate: ItemDelegate {
				text: title
				width: parent.width
			}
		}

		// Main content area
		ColumnLayout {
			Layout.fillWidth: true
			Layout.fillHeight: true

			// Main text area
			TextArea {
				id: chatArea
				Layout.fillWidth: true
				Layout.fillHeight: true
				readOnly: true
				wrapMode: TextEdit.Wrap
			}

			// Text input and send button
			RowLayout {
				Layout.fillWidth: true

				TextField {
					id: messageInput
					Layout.fillWidth: true
					placeholderText: "Type your message here..."
					onAccepted: sendMessage()
				}

				Button {
					text: "Send"
					onClicked: sendMessage()
				}
			}
		}
	}

	Connections {
		target: chatClient

		function onMessageReceived(message) {
			chatArea.append(message)
		}
	}
}