from flask import Flask, jsonify, render_template
from pokeapi import get_berry_data
from statistics import calculate_stats, create_histogram

app = Flask(__name__)

@app.route('/allBerryStats', methods=['GET'])
def all_berry_stats():
    try:
        berry_data = get_berry_data()
        stats = calculate_stats(berry_data)
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/allBerryHistogram', methods=['GET'])
def all_berry_histogram():
    try:
        berry_data = get_berry_data()
        stats = calculate_stats(berry_data)
        histogram_filename = 'histogram.png'
        create_histogram(stats['frequency_growth_time'], 'static/' + histogram_filename)
        return render_template('stats.html', stats=stats, histogram_filename=histogram_filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)