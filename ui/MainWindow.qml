import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

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
		ColumnLayout {
			width: 200

			Button {
				text: "New Chat"
				Layout.fillWidth: true
				onClicked: chatClient.createNewChat("New Chat")
			}

			ListView {
				Layout.fillWidth: true
				Layout.fillHeight: true
				model: chatClient.threadList
				delegate: Item {
					Text { text: modelData.title }
				}
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