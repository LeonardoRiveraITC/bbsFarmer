{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  name = "pipzone";
  packages =[
        pkgs.python310
        pkgs.python310Packages.keyboard
        pkgs.python310Packages.opencv3
        pkgs.python310Packages.pyautogui
        pkgs.python310Packages.tkinter
        pkgs.scrot
  ];
}
