document.addEventListener('DOMContentLoaded', () => {
            // Get references to elements
            const themeToggle = document.getElementById('theme-toggle');
            const body = document.body;
            const tokenForm = document.getElementById('token-form');
            const meterInput = document.getElementById('meter-no');
            const amountInput = document.getElementById('amount');
            const clearButton = document.getElementById('clear-btn');
            const tokenDisplay = document.getElementById('token-display');
            const messageArea = document.getElementById('message-area');
            const statusBar = document.getElementById('status-bar');

            // clear token and message area on page load
            tokenDisplay.textContent = '';
            messageArea.textContent = '';

            const defaultTokenText = 'Your generated token will appear here.';
            tokenDisplay.textContent = defaultTokenText;

            // --- THEME TOGGLE LOGIC ---
            // Function to set the theme
            const setTheme = (theme) => {
                body.classList.toggle('dark-mode', theme === 'dark');
                themeToggle.textContent = theme === 'dark' ? '☀️' : '🌑';
                localStorage.setItem('theme', theme);
            };

            // Event listener for the toggle button
            themeToggle.addEventListener('click', () => {
                const currentTheme = body.classList.contains('dark-mode') ? 'dark' : 'light';
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                setTheme(newTheme);
            });

            // Load saved theme from localStorage on page load
            const savedTheme = localStorage.getItem('theme') || 'light';
            setTheme(savedTheme);


            // --- FORM LOGIC ---
            clearButton.addEventListener('click', () => {
                meterInput.value = '';
                amountInput.value = '';
                tokenDisplay.textContent = defaultTokenText;
                messageArea.textContent = '';
                statusBar.textContent = 'Cleared';
            });

            tokenForm.addEventListener('submit', (event) => {
                event.preventDefault();
                const meterNo = meterInput.value;
                const amount = parseFloat(amountInput.value);

                if (!meterNo || isNaN(amount) || amount <= 0) {
                    messageArea.textContent = 'Please enter a valid meter number and amount.';
                    messageArea.style.color = 'var(--primary-red)';
                    statusBar.textContent = 'Error: Invalid input';
                    return;
                }
                
                messageArea.textContent = '';
                statusBar.textContent = 'Generating token...';
                
                setTimeout(() => {
                    const randomPart = Math.random().toString(36).substring(2, 10).toUpperCase();
                    const fakeToken = `${meterNo}-${randomPart}-${Date.now() % 10000}`;
                    
                    tokenDisplay.textContent = fakeToken;
                    messageArea.textContent = `Token for ${meterNo} successfully created.`;
                    messageArea.style.color = 'var(--primary-blue)';
                    statusBar.textContent = 'Success!';
                }, 500);
            });
        });