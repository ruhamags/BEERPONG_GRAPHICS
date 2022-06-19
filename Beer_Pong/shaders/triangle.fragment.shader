// #version 330 core


// in vec3 newColor;
// // in vec2 outTextCood;


// out vec4 color;
// // uniform sampler2D texSampler;
// // out vec4 color;

// void main()
// {
//     color = vec4(newColor, 1.0);
//     //  outColor = vec4(newColor, 1.0);
//     //  outColor = texture(texSampler, outTextCood);
// }

// *********************************************

#version 330 core


in vec3 newColor;
in vec2 outTextCood;


out vec4 outColor;
uniform sampler2D texSampler;
// out vec4 color;

void main()
{
    // color = vec4(newColor, 1.0);
     outColor = vec4(newColor, 1.0);
     outColor = texture(texSampler, outTextCood);
}