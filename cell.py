import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.selected = False
        self.sketched = False

    def set(self, val):
        self.value = val

    def draw(self, screen):
        chip_font = pygame.font.Font(None, 70)
        sketch_font = pygame.font.Font(None, 35)
        chip_one_surf = chip_font.render('1', 0, CROSS_COLOR)
        chip_one_sketch_surf = sketch_font.render('1', 0, CIRCLE_COLOR)
        chip_two_surf = chip_font.render('2', 0, CROSS_COLOR)
        chip_two_sketch_surf = sketch_font.render('2', 0, CIRCLE_COLOR)
        chip_three_surf = chip_font.render('3', 0, CROSS_COLOR)
        chip_three_sketch_surf = sketch_font.render('3', 0, CIRCLE_COLOR)
        chip_four_surf = chip_font.render('4', 0, CROSS_COLOR)
        chip_four_sketch_surf = sketch_font.render('4', 0, CIRCLE_COLOR)
        chip_five_surf = chip_font.render('5', 0, CROSS_COLOR)
        chip_five_sketch_surf = sketch_font.render('5', 0, CIRCLE_COLOR)
        chip_six_surf = chip_font.render('6', 0, CROSS_COLOR)
        chip_six_sketch_surf = sketch_font.render('6', 0, CIRCLE_COLOR)
        chip_seven_surf = chip_font.render('7', 0, CROSS_COLOR)
        chip_seven_sketch_surf = sketch_font.render('7', 0, CIRCLE_COLOR)
        chip_eight_surf = chip_font.render('8', 0, CROSS_COLOR)
        chip_eight_sketch_surf = sketch_font.render('8', 0, CIRCLE_COLOR)
        chip_nine_surf = chip_font.render('9', 0, CROSS_COLOR)
        chip_nine_sketch_surf = sketch_font.render('9', 0, CIRCLE_COLOR)

        if self.selected:
            pygame.draw.rect(screen, (150, 10, 1), pygame.Rect(self.col * SQUARE_SIZE + 56, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 12)
            self.selected = False

        if not self.selected:
            if self.value == 1:
                chip_one_rect = chip_one_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_one_surf, chip_one_rect)
            elif self.value == 2:
                chip_two_rect = chip_two_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_two_surf, chip_two_rect)
            elif self.value == 3:
                chip_three_rect = chip_three_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_three_surf, chip_three_rect)
            elif self.value == 4:
                chip_four_rect = chip_four_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_four_surf, chip_four_rect)
            elif self.value == 5:
                chip_five_rect = chip_five_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_five_surf, chip_five_rect)
            elif self.value == 6:
                chip_six_rect = chip_six_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_six_surf, chip_six_rect)
            elif self.value == 7:
                chip_seven_rect = chip_seven_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_seven_surf, chip_seven_rect)
            elif self.value == 8:
                chip_eight_rect = chip_eight_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_eight_surf, chip_eight_rect)
            elif self.value == 9:
                chip_nine_rect = chip_nine_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col + 56, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row + 3))
                screen.blit(chip_nine_surf, chip_nine_rect)
        else:
            if self.value == 1:
                chip_one_rect = chip_one_sketch_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_one_sketch_surf, chip_one_rect)
            elif self.value == 2:
                chip_two_rect = chip_two_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_two_sketch_surf, chip_two_rect)
            elif self.value == 3:
                chip_three_rect = chip_three_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_three_sketch_surf, chip_three_rect)
            elif self.value == 4:
                chip_four_rect = chip_four_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_four_sketch_surf, chip_four_rect)
            elif self.value == 5:
                chip_five_rect = chip_five_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_five_sketch_surf, chip_five_rect)
            elif self.value == 6:
                chip_six_rect = chip_six_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_six_sketch_surf, chip_six_rect)
            elif self.value == 7:
                chip_seven_rect = chip_seven_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_seven_sketch_surf, chip_seven_rect)
            elif self.value == 8:
                chip_eight_rect = chip_eight_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_eight_sketch_surf, chip_eight_rect)
            elif self.value == 9:
                chip_nine_rect = chip_nine_sketch_surf.get_rect(
                    center=(SQUARE_SIZE//2+SQUARE_SIZE*self.col - 10 + 56, SQUARE_SIZE//2+SQUARE_SIZE*self.row - 10 + 3))
                screen.blit(chip_nine_sketch_surf, chip_nine_rect)

