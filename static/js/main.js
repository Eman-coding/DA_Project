// Fake Product Reviews Detection - Main JavaScript

// Navigate to product review page
function selectProduct(productId) {
    window.location.href = `/review/${productId}`;
}

// Analyze review function
async function analyzeReview(productId) {
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:9',message:'analyzeReview called',data:{productId:productId},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'A,F'})}).catch(()=>{});
    // #endregion
    
    const reviewText = document.getElementById('review-text').value.trim();
    const loadingDiv = document.getElementById('loading');
    const resultSection = document.getElementById('result-section');
    
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:15',message:'DOM elements check',data:{reviewText:reviewText,loadingDiv:!!loadingDiv,resultSection:!!resultSection},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'C'})}).catch(()=>{});
    // #endregion
    
    // Validate input
    if (!reviewText) {
        alert('Please enter a review to analyze.');
        return;
    }
    
    // Show loading, hide results
    loadingDiv.classList.remove('hidden');
    resultSection.classList.add('hidden');
    
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:25',message:'Before fetch request',data:{url:'/predict',method:'POST'},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'A'})}).catch(()=>{});
    // #endregion
    
    try {
        // Send request to backend
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                review: reviewText,
                product_id: productId
            })
        });
        
        // #region agent log
        fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:40',message:'Fetch response received',data:{status:response.status,statusText:response.statusText,ok:response.ok},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'A,G'})}).catch(()=>{});
        // #endregion
        
        const data = await response.json();
        
        // #region agent log
        fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:43',message:'Response data parsed',data:{hasLabel:'label' in data,hasFakeProb:'fake_probability' in data,hasRealProb:'real_probability' in data,dataKeys:Object.keys(data)},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'B'})}).catch(()=>{});
        // #endregion
        
        if (response.ok) {
            // Hide loading, show results
            loadingDiv.classList.add('hidden');
            displayResults(data);
        } else {
            // #region agent log
            fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:50',message:'Response not OK',data:{error:data.error,status:response.status},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'G'})}).catch(()=>{});
            // #endregion
            alert('Error: ' + (data.error || 'Failed to analyze review'));
            loadingDiv.classList.add('hidden');
        }
    } catch (error) {
        // #region agent log
        fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:56',message:'Exception caught',data:{errorMessage:error.message,errorName:error.name},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'F'})}).catch(()=>{});
        // #endregion
        console.error('Error:', error);
        alert('An error occurred while analyzing the review.');
        loadingDiv.classList.add('hidden');
    }
}

// Display prediction results
function displayResults(data) {
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:58',message:'displayResults called',data:{hasLabel:'label' in data,hasFakeProb:'fake_probability' in data,hasRealProb:'real_probability' in data},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'B'})}).catch(()=>{});
    // #endregion
    
    const resultSection = document.getElementById('result-section');
    const resultLabel = document.getElementById('result-label');
    const reviewDisplayText = document.getElementById('review-display-text');
    
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:65',message:'DOM elements in displayResults',data:{resultSection:!!resultSection,resultLabel:!!resultLabel,reviewDisplayText:!!reviewDisplayText},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'C'})}).catch(()=>{});
    // #endregion
    
    // Show result section
    resultSection.classList.remove('hidden');
    
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:70',message:'After removing hidden class',data:{hasHiddenClass:resultSection.classList.contains('hidden'),computedDisplay:window.getComputedStyle(resultSection).display},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'E'})}).catch(()=>{});
    // #endregion
    
    // Set result label
    const isFake = data.label === 'FAKE REVIEW';
    resultLabel.textContent = data.label;
    resultLabel.className = 'result-label ' + (isFake ? 'fake' : 'real');
    
    // Display review text
    reviewDisplayText.textContent = data.review_text;
    
    // Create chart
    createChart(data.fake_probability, data.real_probability);
    
    // Scroll to results
    resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Create Chart.js visualization
function createChart(fakeProb, realProb) {
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:82',message:'createChart called',data:{fakeProb:fakeProb,realProb:realProb,chartAvailable:typeof Chart !== 'undefined'},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch(()=>{});
    // #endregion
    
    const canvas = document.getElementById('chart-canvas');
    const container = document.getElementById('result-chart');
    
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:87',message:'Chart canvas check',data:{canvas:!!canvas,container:!!container},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'C,D'})}).catch(()=>{});
    // #endregion
    
    // Clear previous chart if exists
    if (window.chartInstance) {
        window.chartInstance.destroy();
    }
    
    const ctx = canvas.getContext('2d');
    
    // #region agent log
    fetch('http://127.0.0.1:7245/ingest/ee585ff1-eeca-4662-86d5-a2894d6e3f09',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:95',message:'Before Chart creation',data:{ctx:!!ctx,ChartAvailable:typeof Chart !== 'undefined'},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch(()=>{});
    // #endregion
    
    window.chartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Fake', 'Real'],
            datasets: [{
                label: 'Probability (%)',
                data: [
                    parseFloat((fakeProb * 100).toFixed(1)),
                    parseFloat((realProb * 100).toFixed(1))
                ],
                backgroundColor: [
                    'rgba(198, 40, 40, 0.8)',
                    'rgba(46, 125, 50, 0.8)'
                ],
                borderColor: [
                    'rgba(198, 40, 40, 1)',
                    'rgba(46, 125, 50, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.parsed.y.toFixed(1) + '%';
                        }
                    }
                }
            }
        }
    });
}

// Reset form
function resetForm() {
    document.getElementById('review-text').value = '';
    document.getElementById('result-section').classList.add('hidden');
    document.getElementById('review-text').focus();
    
    // Destroy chart
    if (window.chartInstance) {
        window.chartInstance.destroy();
        window.chartInstance = null;
    }
}
