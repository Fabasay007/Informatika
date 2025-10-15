#include <SFML/Graphics.hpp>

int main() { 


const int cellSize = 50;
const int gridSize = 10;
sf::RenderWindow window(sf::VideoMode(500, 500),"gfjfg" );
while (window.isOpen()){


        // Обрабатываем события в цикле
sf::Event event;

sf::RectangleShape cells[gridSize][gridSize];
for (int i = 0; i < gridSize; i++){
  for ( int j = 0; j < gridSize; ++j){
    cells[i][j].setSize(sf::Vector2f(cellSize -2, cellSize -2));
    cells[i][j].setPosition(i* cellSize, j * cellSize);
    cells[i][j].setFillColor(sf::Color::White);
    cells[i][j].setOutlineColor(sf::Color::Black);
    cells[i][j].setOutlineThickness(1); 
    
    if (i+j>gridSize-1 and j%2!=0){
        cells[i][j].setFillColor(sf::Color::Green);
        cells[i][j].setOutlineColor(sf::Color::Black);
    }

  }




}
while(window.pollEvent(event)){

  if(event.type == sf::Event::Closed){
    window.close();
  }
}

window.clear(sf::Color::White);

for (int i = 0; i < gridSize;++i){
  for (int j = 0; j< gridSize;++j){
    window.draw(cells[i][j]);

  }
}
window.display();
}
return 0;
}