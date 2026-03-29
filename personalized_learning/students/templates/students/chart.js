<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<canvas id="gradeChart"></canvas>
<script>
var ctx = document.getElementById('gradeChart').getContext('2d');
var gradeChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [{% for perf in performances %}'{{ perf.date_recorded|date:"Y-m-d" }}',{% endfor %}],
        datasets: [{
            label: 'Predicted G3',
            data: [{% for perf in performances %}{{ perf.predicted_G3 }},{% endfor %}],
            borderColor: 'blue',
            fill: false
        }]
    }
});
</script>