{pkgs? import<nixpkgs>{}}:
let 
py = with pkgs; [
   (python38.withPackages(ps: with ps; [ keyboard pyautogui xlib]))
  ];
in 
pkgs.mkShell{
    name="auopy devenv"; 
    packages=[
        py
        pkgs.scrot
    ];
    shellHook=''
       echo "Entorno de desarrollo listo" 
    '';
}

