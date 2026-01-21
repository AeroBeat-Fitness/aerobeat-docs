# Audio Conductor

We do not use `_process(delta)` for rhythm timing.

* **Time Source:** `AudioServer.get_dsp_time()` + `AudioServer.get_time_since_last_mix()`.
* **Latency:** Visual spawn times are offset by a user-calibrated `latency_ms`.
* **Signals:** The Conductor emits `beat_hit(beat_index)`. Spawners listen to signals; they do not count time themselves.