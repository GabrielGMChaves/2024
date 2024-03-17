library(ggplot2)
library(palmerpenguins)

ggplot(data=penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm, y=body_mass_g))+
  geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g))

ggplot(data=penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm, y=body_mass_g, linetype=species))

ggplot(data=penguins)+
  geom_jitter(mapping = aes(x=flipper_length_mm, y=body_mass_g))


ggplot(data = diamonds)+
  geom_bar(mapping = aes(x = clarity, fill = clarity))


ggplot(data = diamonds)+
  geom_bar(mapping = aes(x = cut, fill = clarity))

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g))+
  facet_wrap(~species)

ggplot(data = diamonds)+
  geom_bar(mapping = aes(x = color, fill = cut))+
  facet_wrap(~cut)

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species))+
  labs(title="Penguins: Body Mass vs Flipper length",subtitle = "Test",caption = "Made By: Gabriel C.")+
  annotate("text", x=220,y = 3500, label="The Gentoos are the largest!",
           fontface="bold",size=3.5, angle=25)
  
    
