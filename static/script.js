// static/script.js
$(document).ready(function() {
    // Selectors
    var chatbotContainer = $('#chatbot-container');
    var chatbotHeader = $('#chatbot-header');
    var chatbotBody = $('#chatbot-body');
    var chatbotInput = $('#chatbot-input');
    var chatbotSendBtn = $('#chatbot-send-btn');

    // Function to send user input to the server
    function sendUserInputToServer(userInput) {
        $.ajax({
            type: 'POST',
            url: '/predict_emotion',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ text: userInput }),
            success: function(response) {
                // Check if the 'emotion' property exists in the response
                if ('emotion' in response) {
                    var emotion = response.emotion;
                    displayMessage("Bot: I detected you're feeling " + emotion + ".", 'bot');
                
                    // Check if the emotion is sad or confused
                    if (emotion.toLowerCase() === 'sad') {
                        displayMessage("Bot: It seems like you're feeling sad. How about taking a rest or listening to some uplifting music?", 'bot');
                    } else if (emotion.toLowerCase() === 'confused') {
                        displayMessage("Bot: It looks like you're feeling confused. Maybe take a break, play some calming music, or talk to a friend for support.", 'bot');
                    }
                }
                else {
                    console.error('Error: Emotion not found in the response.');
                    displayMessage('Bot: Error predicting emotion. Check the console for details.', 'bot');
                }
            },
            error: function(xhr, status, error) {
                console.error('Error predicting emotion:', error);

                // Display more information about the error
                displayMessage('Bot: Error predicting emotion. Check the console for details.', 'bot');

                // Log detailed error information to the console
                console.error('XHR status:', status);
                console.error('XHR response:', xhr.responseText);
            }
        });
    }

    // Function to display a message in the chatbot
    function displayMessage(message, sender) {
        var messageDiv = $('<div>').text(message).addClass('chat-message');
        if (sender === 'bot') {
            messageDiv.addClass('bot-message');
        } else {
            messageDiv.addClass('user-message');
        }
        chatbotBody.append(messageDiv);
        chatbotBody.scrollTop(chatbotBody.prop('scrollHeight'));
    }

    // Function to handle user input
    function handleUserInput() {
        var userInput = chatbotInput.val().trim();
        if (userInput !== '') {
            displayMessage("You: " + userInput, 'user');
            sendUserInputToServer(userInput);
            chatbotInput.val('');
        }
    }

    // Event handlers
    chatbotHeader.click(function() {
        chatbotBody.slideToggle();
    });

    chatbotSendBtn.click(function() {
        handleUserInput();
    });

    chatbotInput.keypress(function(event) {
        if (event.which === 13) { // Enter key pressed
            handleUserInput();
        }
    });
});
