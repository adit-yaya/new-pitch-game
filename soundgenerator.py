import pygame
import random
import numpy as np

class SoundGenerator:
    def __init__(self):
        self.sample_rate = 44100
        self.duration = 0.18
        self.volume = 0.275

    def generate_sine_wave(self, frequency):
        num_samples = int(self.duration * self.sample_rate)
        time = np.linspace(0, self.duration, num_samples, endpoint=False)
        sine_wave = np.sin(2 * np.pi * frequency * time)
        normalized_wave = sine_wave * 32767 / np.max(np.abs(sine_wave))
        stereo_wave = np.array([normalized_wave, normalized_wave])  
        stereo_wave_contiguous = np.ascontiguousarray(stereo_wave.T) 
        return pygame.sndarray.make_sound(stereo_wave_contiguous.astype(np.int16))

    def generate_noise(self):
        num_samples = int(self.duration * self.sample_rate)
        noise = np.random.uniform(-1, 1, num_samples)
        normalized_noise = noise * 32767
        stereo_noise = np.array([normalized_noise, normalized_noise])
        stereo_noise_contiguous = np.ascontiguousarray(stereo_noise.T)  
        return pygame.sndarray.make_sound(stereo_noise_contiguous.astype(np.int16))

    def fadeout_sound(self, sound, fadeout_duration=1000):
        current_volume = sound.get_volume()
        fadeout_steps = int(fadeout_duration / 100)
        volume_step = current_volume / fadeout_steps
        for _ in range(fadeout_steps):
            current_volume -= volume_step
            if current_volume < 0:
                current_volume = 0
            sound.set_volume(current_volume)
            pygame.time.wait(10)

    def play_sound(self):
        t = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 3000:
            freq = random.uniform(400.0, 1000.0)
            sine_wave = self.generate_sine_wave(freq)
            noise = self.generate_noise()
            sine_wave.play()
            noise.play()
            self.fadeout_sound(sine_wave)
            self.fadeout_sound(noise)
            t.tick_busy_loop(5)
