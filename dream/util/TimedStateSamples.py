class TimedStateSample:
    def __init__(self, current_time, decay_values, token_counts, marking, place_list):
        self.data = {'current_time' : current_time}

        decay_vector = []
        token_count_vector = []
        marking_vector = []

        for place in place_list:
            decay_vector.append(decay_values[str(place)])
            token_count_vector.append(token_counts[str(place)])

            if place in marking:
                marking_vector.append(1)
            else:
                marking_vector.append(0)

        self.data["TimedStateSample"] = [decay_vector, token_count_vector, marking_vector]

    def setRecentEvent(self, event):
        self.data["recentEvent"] = event

    def setNextEvent(self, event):
        self.data["nextEvent"] = event

    def export(self):
        return self.data
